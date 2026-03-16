import os
import subprocess
import warnings
import urllib.request
import urllib.error

# App version - keep in sync with setup.py CFBundleVersion
APP_VERSION = "1.4.0"
GITHUB_REPO = "leedale30/abc-to-xml-converter"

# Suppress pyparsing deprecation warnings (abc2xml uses old API)
warnings.filterwarnings('ignore', category=DeprecationWarning, module='pyparsing')

from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)

# Disable caching for all responses
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

import sys
import json
import re

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# Path to the abc2xml converter script
CONVERTER_SCRIPT = resource_path(os.path.join('abc2xml', 'abc2xml.py'))

# Load annotation guide
GUIDE_PATH = resource_path('annotationguide.json')
try:
    with open(GUIDE_PATH, 'r', encoding='utf-8') as f:
        ANNOTATION_GUIDE = json.load(f)
    print(f"Loaded annotation guide with {len(ANNOTATION_GUIDE.get('directives', {}))} directives", file=sys.stderr)
except Exception as e:
    print(f"Warning: Could not load annotation guide: {e}", file=sys.stderr)
    ANNOTATION_GUIDE = {}

def preprocess_abc(content):
    if not ANNOTATION_GUIDE:
        return content

    lines = content.splitlines()
    processed_lines = []
    
    # Regex to match directives: %%name key=value ...
    # This is a basic parser.
    directive_pattern = re.compile(r'^%%\s*(\w+)\s*(.*)$')
    
    print("Preprocessing content...", file=sys.stderr)

    for line in lines:
        match = directive_pattern.match(line)
        if match:
            name = match.group(1)
            args_str = match.group(2)
            print(f"Found directive: {name} args={args_str}", file=sys.stderr)
            
            if name in ANNOTATION_GUIDE.get('directives', {}):
                definition = ANNOTATION_GUIDE['directives'][name]
                
                # Parse attributes from args_str (simple space separated key=value)
                # This might need to be more robust if values contain spaces.
                # Assuming simple format for now based on user examples if any.
                # Actually, the user didn't give examples of usage, just the JSON.
                # Standard ABC directives usually look like %%name value or %%name param=value
                
                # Logic based on directive type
                xml_mapping = definition.get('musicXML')
                
                if xml_mapping is None:
                    # Ignore this directive (remove line)
                    print(f"Ignoring directive {name} (no XML mapping)", file=sys.stderr)
                    continue
                
                if xml_mapping.get('element') == 'direction':
                    # Handle direction elements
                    dir_type = xml_mapping.get('type', 'words')
                    if dir_type == 'words':
                        # Convert to text annotation: "args_str" or specific formatting
                        # Replace inner double quotes with single quotes to avoid breaking ABC string syntax
                        safe_args = args_str.replace('"', "'")
                        new_line = f'"{name}: {safe_args}"'
                        print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                        processed_lines.append(new_line)
                    elif dir_type == 'rehearsal':
                        # Handle rehearsal marks
                        new_line = f'"^[{args_str.strip()}]"'
                        print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                        processed_lines.append(new_line)
                    elif dir_type == 'effect':
                        # Handle effects
                        safe_args = args_str.replace('"', "'")
                        new_line = f'"!{name}: {safe_args}!"'
                        print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                        processed_lines.append(new_line)
                elif xml_mapping.get('element') == 'notations' and xml_mapping.get('type') == 'articulations':
                     # Decorator: %%art type=staccato -> !staccato!
                     # expecting args like type="staccato"
                     # Simple parsing for 'type='
                     type_match = re.search(r'type=["\']?(\w+)["\']?', args_str)
                     if type_match:
                         deco_value = type_match.group(1)
                         new_line = f'!{deco_value}!'
                         print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                         processed_lines.append(new_line)
                     else:
                         # Fallback if parsing fails? maintain original or warn?
                         # For now, append nothing to avoid breaking functionality
                         print(f"Failed to parse type for {name}", file=sys.stderr)
                         pass
                elif xml_mapping.get('element') == 'sound':
                    # Handle sound elements like swing and mute
                    sound_type = xml_mapping.get('type')
                    sound_value = xml_mapping.get('value')
                    if sound_type and sound_value:
                        new_line = f'"!{sound_type}: {sound_value}!"'
                        print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                        processed_lines.append(new_line)
                elif xml_mapping.get('element') == 'harmony':
                    # Handle harmony elements like frame and analysis
                    harm_type = xml_mapping.get('type')
                    if harm_type == 'frame':
                        # Handle guitar chord frames
                        new_line = f'"!frame: {args_str}!"'
                        print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                        processed_lines.append(new_line)
                    elif harm_type == 'function':
                        # Handle harmonic analysis
                        new_line = f'"!analysis: {args_str}!"'
                        print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                        processed_lines.append(new_line)
                elif xml_mapping.get('element') == 'figured-bass':
                    # Handle figured bass
                    new_line = f'"!fb: {args_str}!"'
                    print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                    processed_lines.append(new_line)
                elif xml_mapping.get('element') == 'print':
                    # Handle print elements like newpage, newline, measurenumbering
                    print_type = xml_mapping.get('type')
                    if print_type:
                        new_line = f'"!print: {print_type}!"'
                        print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                        processed_lines.append(new_line)
                elif xml_mapping.get('element') == 'system-distance':
                    # Handle vertical spacing
                    new_line = f'"!vskip: {args_str}!"'
                    print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                    processed_lines.append(new_line)
                elif xml_mapping.get('element') == 'system-dividers':
                    # Handle separators
                    new_line = '"!sep!"'
                    print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                    processed_lines.append(new_line)
                elif xml_mapping.get('element') == 'repeat':
                    # Handle loop directive
                    new_line = '"!loop!"'
                    print(f"Mapped {name} to: {new_line}", file=sys.stderr)
                    processed_lines.append(new_line)
                else:
                    # Unknown mapping type, keep original or ignore?
                    # Keep original for safety if it might be valid ABC we don't know
                    print(f"Unknown mapping for {name}, keeping original", file=sys.stderr)
                    processed_lines.append(line)
            else:
                # Not a custom directive we know, keep it (e.g. %%score)
                # print(f"Unknown directive {name}, keeping original", file=sys.stderr)
                processed_lines.append(line)
        else:
            processed_lines.append(line)
            
    return '\n'.join(processed_lines)

@app.route('/')
def index():
    return render_template('index.html', version=APP_VERSION)

@app.route('/convert', methods=['POST'])
def convert():
    try:
        abc_content = request.json.get('abc_content')
        if not abc_content:
            return jsonify({'error': 'No content provided'}), 400

        # Preprocess content
        abc_content = preprocess_abc(abc_content)

        # Create a temporary file or pass input via stdin? 
        # abc2xml.py usually takes a filename.
        # Let's write to a temporary file.
        import tempfile
        
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False, encoding='utf-8') as temp_abc:
            temp_abc.write(abc_content)
            temp_abc_path = temp_abc.name

        try:
            # Run the converter
            # abc2xml writes to stdout by default if no output file specified?
            # Wait, usually `python abc2xml.py file.abc` prints to stdout.
            # But earlier usage was `> output.xml`.
            # So yes, capture stdout.
            
            result = subprocess.run(
                [sys.executable, CONVERTER_SCRIPT, temp_abc_path],
                capture_output=True,
                text=True,
                encoding='utf-8',
                check=False # Don't raise exception immediately, we want to capture stderr
            )
            
            if result.returncode != 0:
                # Converter failed
                return jsonify({'error': result.stderr or 'Unknown error occurred'}), 500
            
            xml_output = result.stdout
            return jsonify({
                'xml_content': xml_output,
                'logs': result.stderr
            })
            
        finally:
            # Clean up temp file
            if os.path.exists(temp_abc_path):
                os.remove(temp_abc_path)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save', methods=['POST'])
def save_session():
    try:
        data = request.json
        abc_content = data.get('abc_content', '')
        xml_content = data.get('xml_content', '')
        logs = data.get('logs', '')
        
        # Determine folder name
        # Try to find T:Title
        title_match = re.search(r'^T:\s*(.*)$', abc_content, re.MULTILINE)
        if title_match:
            # Sanitize title
            safe_title = re.sub(r'[^\w\-]', '_', title_match.group(1).strip())
        else:
            safe_title = "Untitled"
            
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = f"{timestamp}_{safe_title}"
        
        # Base save directory
        # For saved sessions, we want to stay outside the temp bundle directory if possible,
        # but for simplicity in a portable app, we'll use the user's home directory or the app path.
        # Let's use current working directory or a 'saved_sessions' folder next to the app.
        save_base = os.path.join(os.getcwd(), 'saved_sessions')
        if not os.path.exists(save_base):
            os.makedirs(save_base)
            
        session_dir = os.path.join(save_base, folder_name)
        os.makedirs(session_dir)
        
        # Write files
        with open(os.path.join(session_dir, 'input.abc'), 'w', encoding='utf-8') as f:
            f.write(abc_content)
        
        with open(os.path.join(session_dir, 'output.musicxml'), 'w', encoding='utf-8') as f:
            f.write(xml_content)
            
        with open(os.path.join(session_dir, 'conversion.log'), 'w', encoding='utf-8') as f:
            f.write(logs)
            
        return jsonify({'message': 'Session saved successfully', 'path': session_dir})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/check-update')
def check_update():
    """Check GitHub for a newer release."""
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
        req = urllib.request.Request(url, headers={'User-Agent': 'ABC-Converter'})
        
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        latest_version = data.get('tag_name', '').lstrip('v')
        download_url = data.get('html_url', f'https://github.com/{GITHUB_REPO}/releases')
        
        # Simple version comparison (assumes semantic versioning)
        update_available = latest_version > APP_VERSION if latest_version else False
        
        return jsonify({
            'update_available': update_available,
            'current_version': APP_VERSION,
            'latest_version': latest_version,
            'download_url': download_url
        })
    except Exception as e:
        # Fail silently - don't block app if GitHub is unreachable
        return jsonify({
            'update_available': False,
            'current_version': APP_VERSION,
            'error': str(e)
        })

@app.route('/convert-to', methods=['POST'])
def convert_to():
    """Convert ABC+ to various music file formats."""
    try:
        abc_content = request.json.get('abc_content')
        format = request.json.get('format')
        
        if not abc_content:
            return jsonify({'error': 'No content provided'}), 400
        
        if not format:
            return jsonify({'error': 'No format specified'}), 400
        
        # Preprocess content
        abc_content = preprocess_abc(abc_content)
        
        # Create a temporary file
        import tempfile
        
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False, encoding='utf-8') as temp_abc:
            temp_abc.write(abc_content)
            temp_abc_path = temp_abc.name
        
        try:
            # First convert to MusicXML using abc2xml
            result = subprocess.run(
                [sys.executable, CONVERTER_SCRIPT, temp_abc_path],
                capture_output=True,
                text=True,
                encoding='utf-8',
                check=False
            )
            
            if result.returncode != 0:
                return jsonify({'error': result.stderr or 'Conversion to MusicXML failed'}), 500
            
            xml_content = result.stdout
            
            # Check if format is lilypond, use abc2ly directly
            if format == 'lilypond':
                # Create output path manually
                temp_out_path = temp_abc_path.replace('.abc', '.ly')
                
                # Run abc2ly with explicit output file
                result = subprocess.run(
                    ['abc2ly', '-o', temp_out_path, temp_abc_path],
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    check=False
                )
                
                if result.returncode != 0:
                    # Clean up temporary file
                    if os.path.exists(temp_out_path):
                        os.remove(temp_out_path)
                    return jsonify({'error': result.stderr or 'Conversion to LilyPond failed'}), 500
                
                # Read the output file
                try:
                    with open(temp_out_path, 'rb') as f:
                        output_content = f.read()
                except Exception as e:
                    return jsonify({'error': f'Error reading output file: {e}'}), 500
                
                # Clean up the temporary LilyPond file
                if os.path.exists(temp_out_path):
                    os.remove(temp_out_path)
            else:
                # Use music21 for other formats
                import music21
                
                # Create a temporary XML file
                with tempfile.NamedTemporaryFile(mode='w+', suffix='.xml', delete=False, encoding='utf-8') as temp_xml:
                    temp_xml.write(xml_content)
                    temp_xml_path = temp_xml.name
                
                try:
                    # Parse the MusicXML
                    score = music21.converter.parse(temp_xml_path)
                    
                    # Create another temporary file for the output
                    with tempfile.NamedTemporaryFile(mode='wb', suffix=f'.{format}', delete=False) as temp_out:
                        temp_out_path = temp_out.name
                    
                    # Convert to the requested format
                    score.write(format, temp_out_path)
                    
                    # Read the output file
                    with open(temp_out_path, 'rb') as f:
                        output_content = f.read()
                finally:
                    # Clean up temporary files
                    if os.path.exists(temp_xml_path):
                        os.remove(temp_xml_path)
                    if os.path.exists(temp_out_path):
                        os.remove(temp_out_path)
            
            # Determine MIME type
            mime_types = {
                'midi': 'audio/midi',
                'musicxml': 'application/xml',
                'lilypond': 'text/plain',
                'mei': 'application/xml',
                'abc': 'text/plain'
            }
            
            mime_type = mime_types.get(format, 'application/octet-stream')
            
            # Create response
            response = make_response(output_content)
            response.headers['Content-Type'] = mime_type
            response.headers['Content-Disposition'] = f'attachment; filename=output.{format}'
            
            return response
                    
        finally:
            # Clean up temp file
            if os.path.exists(temp_abc_path):
                os.remove(temp_abc_path)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/convert-to-midi', methods=['POST'])
def convert_to_midi():
    """Convert ABC+ to MIDI using abcmidi."""
    try:
        abc_content = request.json.get('abc_content')
        
        if not abc_content:
            return jsonify({'error': 'No content provided'}), 400
        
        # Preprocess content
        abc_content = preprocess_abc(abc_content)
        
        # Create a temporary file
        import tempfile
        
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False, encoding='utf-8') as temp_abc:
            temp_abc.write(abc_content)
            temp_abc_path = temp_abc.name
        
        try:
            # Create output path for MIDI file
            temp_out_path = temp_abc_path.replace('.abc', '.mid')
            
            # Run abc2midi to convert ABC to MIDI
            result = subprocess.run(
                ['abc2midi', temp_abc_path, '-o', temp_out_path],
                capture_output=True,
                text=True,
                encoding='utf-8',
                check=False
            )
            
            if result.returncode != 0:
                # Clean up temporary file
                if os.path.exists(temp_out_path):
                    os.remove(temp_out_path)
                return jsonify({'error': result.stderr or 'Conversion to MIDI failed'}), 500
            
            # Check if output file exists
            if not os.path.exists(temp_out_path):
                return jsonify({'error': 'MIDI file was not created'}), 500
            
            # Read the output file
            try:
                with open(temp_out_path, 'rb') as f:
                    output_content = f.read()
            except Exception as e:
                return jsonify({'error': f'Error reading output file: {e}'}), 500
            
            # Clean up the temporary MIDI file
            if os.path.exists(temp_out_path):
                os.remove(temp_out_path)
            
            # Create response
            response = make_response(output_content)
            response.headers['Content-Type'] = 'audio/midi'
            response.headers['Content-Disposition'] = 'attachment; filename=output.mid'
            
            return response
                    
        finally:
            # Clean up temp file
            if os.path.exists(temp_abc_path):
                os.remove(temp_abc_path)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/convert-to-lilypond', methods=['POST'])
def convert_to_lilypond():
    """Convert ABC+ to LilyPond using abc2ly."""
    try:
        abc_content = request.json.get('abc_content')
        
        if not abc_content:
            return jsonify({'error': 'No content provided'}), 400
        
        # Preprocess content
        abc_content = preprocess_abc(abc_content)
        
        # Create a temporary file
        import tempfile
        
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False, encoding='utf-8') as temp_abc:
            temp_abc.write(abc_content)
            temp_abc_path = temp_abc.name
        
        try:
            # Create output path for LilyPond file
            temp_out_path = temp_abc_path.replace('.abc', '.ly')
            
            # Run abc2ly to convert ABC to LilyPond
            result = subprocess.run(
                ['abc2ly', '-o', temp_out_path, temp_abc_path],
                capture_output=True,
                text=True,
                encoding='utf-8',
                check=False
            )
            
            if result.returncode != 0:
                # Clean up temporary file
                if os.path.exists(temp_out_path):
                    os.remove(temp_out_path)
                return jsonify({'error': result.stderr or 'Conversion to LilyPond failed'}), 500
            
            # Check if output file exists
            if not os.path.exists(temp_out_path):
                return jsonify({'error': 'LilyPond file was not created'}), 500
            
            # Read the output file
            try:
                with open(temp_out_path, 'r', encoding='utf-8') as f:
                    output_content = f.read()
            except Exception as e:
                return jsonify({'error': f'Error reading output file: {e}'}), 500
            
            # Clean up the temporary LilyPond file
            if os.path.exists(temp_out_path):
                os.remove(temp_out_path)
            
            # Return LilyPond content as JSON
            return jsonify({
                'ly_content': output_content,
                'logs': result.stderr
            })
                    
        finally:
            # Clean up temp file
            if os.path.exists(temp_abc_path):
                os.remove(temp_abc_path)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/convert-to-all', methods=['POST'])
def convert_to_all():
    """Convert ABC+ to all supported music file formats and return as a zip file."""
    try:
        abc_content = request.json.get('abc_content')
        
        if not abc_content:
            return jsonify({'error': 'No content provided'}), 400
        
        # Preprocess content
        processed_abc = preprocess_abc(abc_content)
        
        # Create a temporary directory for conversion files
        import tempfile
        import zipfile
        
        # Create a zip file in memory
        import io
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add original ABC content
            zipf.writestr('input.abc', abc_content)
            
            # Add processed ABC content
            zipf.writestr('processed_input.abc', processed_abc)
            
            # 1. Convert to MusicXML using abc2xml
            xml_content = None
            try:
                # Create a temporary ABC file for conversion
                with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False, encoding='utf-8') as temp_abc:
                    temp_abc.write(processed_abc)
                    temp_abc_path = temp_abc.name
                
                result = subprocess.run(
                    [sys.executable, CONVERTER_SCRIPT, temp_abc_path],
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    check=False
                )
                
                if result.returncode == 0:
                    xml_content = result.stdout
                    zipf.writestr('output.musicxml', xml_content)
                else:
                    print(f"Conversion to MusicXML failed: {result.stderr}", file=sys.stderr)
            except Exception as e:
                print(f"Error during MusicXML conversion: {e}", file=sys.stderr)
            finally:
                # Clean up temporary ABC file
                if 'temp_abc_path' in locals() and os.path.exists(temp_abc_path):
                    os.remove(temp_abc_path)
            
            # 2. Convert to MIDI using abc2midi
            try:
                # Create a temporary ABC file for conversion
                with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False, encoding='utf-8') as temp_abc:
                    temp_abc.write(processed_abc)
                    temp_abc_path = temp_abc.name
                
                # Create output path for MIDI file
                midi_path = temp_abc_path.replace('.abc', '.mid')
                
                result = subprocess.run(
                    ['abc2midi', temp_abc_path, '-o', midi_path],
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    check=False
                )
                
                if result.returncode == 0 and os.path.exists(midi_path):
                    # Read the MIDI file and add it to the zip
                    with open(midi_path, 'rb') as f:
                        midi_content = f.read()
                    zipf.writestr('output.mid', midi_content)
                else:
                    print(f"Conversion to MIDI failed: {result.stderr}", file=sys.stderr)
            except Exception as e:
                print(f"Error during MIDI conversion: {e}", file=sys.stderr)
            finally:
                # Clean up temporary files
                if 'temp_abc_path' in locals() and os.path.exists(temp_abc_path):
                    os.remove(temp_abc_path)
                if 'midi_path' in locals() and os.path.exists(midi_path):
                    os.remove(midi_path)
            
            # 3. Convert to LilyPond using abc2ly
            try:
                # Create a temporary ABC file for conversion
                with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False, encoding='utf-8') as temp_abc:
                    temp_abc.write(processed_abc)
                    temp_abc_path = temp_abc.name
                
                # Create output path for LilyPond file
                ly_path = temp_abc_path.replace('.abc', '.ly')
                
                result = subprocess.run(
                    ['abc2ly', '-o', ly_path, temp_abc_path],
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    check=False
                )
                
                if result.returncode == 0 and os.path.exists(ly_path):
                    # Read the LilyPond file and add it to the zip
                    with open(ly_path, 'r', encoding='utf-8') as f:
                        ly_content = f.read()
                    zipf.writestr('output.ly', ly_content)
                else:
                    print(f"Conversion to LilyPond failed: {result.stderr}", file=sys.stderr)
            except Exception as e:
                print(f"Error during LilyPond conversion: {e}", file=sys.stderr)
            finally:
                # Clean up temporary files
                if 'temp_abc_path' in locals() and os.path.exists(temp_abc_path):
                    os.remove(temp_abc_path)
                if 'ly_path' in locals() and os.path.exists(ly_path):
                    os.remove(ly_path)
            
            # 4. Use music21 for additional formats if MusicXML was successful
            if xml_content:
                try:
                    import music21
                    
                    # Create a temporary XML file
                    with tempfile.NamedTemporaryFile(mode='w+', suffix='.xml', delete=False, encoding='utf-8') as temp_xml:
                        temp_xml.write(xml_content)
                        temp_xml_path = temp_xml.name
                    
                    try:
                        # Parse the MusicXML
                        score = music21.converter.parse(temp_xml_path)
                        
                        # Additional formats
                        additional_formats = ['abc']
                        for format in additional_formats:
                            try:
                                # Create a temporary file for output
                                with tempfile.NamedTemporaryFile(mode='wb', suffix=f'.{format}', delete=False) as temp_out:
                                    temp_out_path = temp_out.name
                                
                                # Write the output
                                score.write(format, temp_out_path)
                                
                                # Read the output and add it to the zip
                                if os.path.exists(temp_out_path):
                                    if format == 'abc':
                                        with open(temp_out_path, 'r', encoding='utf-8') as f:
                                            content = f.read()
                                    else:
                                        with open(temp_out_path, 'rb') as f:
                                            content = f.read()
                                    zipf.writestr(f'output.{format}', content)
                            except Exception as e:
                                print(f"Failed to convert to {format}: {e}", file=sys.stderr)
                                # Skip this format and continue with others
                                continue
                            finally:
                                # Clean up temporary output file
                                if 'temp_out_path' in locals() and os.path.exists(temp_out_path):
                                    os.remove(temp_out_path)
                    finally:
                        # Clean up temporary XML file
                        if os.path.exists(temp_xml_path):
                            os.remove(temp_xml_path)
                except Exception as e:
                    print(f"Error during music21 conversions: {e}", file=sys.stderr)
        
        # Rewind the buffer to the beginning
        zip_buffer.seek(0)
        
        # Get the zip content
        zip_content = zip_buffer.getvalue()
        
        # Create response
        response = make_response(zip_content)
        response.headers['Content-Type'] = 'application/zip'
        response.headers['Content-Disposition'] = 'attachment; filename=all_formats.zip'
        
        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Format information mapping
FORMAT_INFO = {
    'abc': {'name': 'ABC Notation', 'ext': 'abc', 'mime': 'text/plain', 'can_read': True, 'can_write': True},
    'musicxml': {'name': 'MusicXML', 'ext': 'xml', 'mime': 'application/xml', 'can_read': True, 'can_write': True},
    'mxl': {'name': 'Compressed MusicXML', 'ext': 'mxl', 'mime': 'application/vnd.recordare.musicxml', 'can_read': True, 'can_write': True},
    'midi': {'name': 'MIDI', 'ext': 'mid', 'mime': 'audio/midi', 'can_read': True, 'can_write': True},
    'mid': {'name': 'MIDI', 'ext': 'mid', 'mime': 'audio/midi', 'can_read': True, 'can_write': True},
    'lilypond': {'name': 'LilyPond', 'ext': 'ly', 'mime': 'text/plain', 'can_read': True, 'can_write': False},
    'ly': {'name': 'LilyPond', 'ext': 'ly', 'mime': 'text/plain', 'can_read': True, 'can_write': False},
    'mei': {'name': 'MEI', 'ext': 'mei', 'mime': 'application/xml', 'can_read': True, 'can_write': False},
    'capella': {'name': 'Capella', 'ext': 'cap', 'mime': 'application/octet-stream', 'can_read': True, 'can_write': False},
    'cap': {'name': 'Capella', 'ext': 'cap', 'mime': 'application/octet-stream', 'can_read': True, 'can_write': False},
    'noteworthy': {'name': 'NoteWorthy Composer Text', 'ext': 'nwctxt', 'mime': 'text/plain', 'can_read': True, 'can_write': True},
    'nwctxt': {'name': 'NoteWorthy Composer Text', 'ext': 'nwctxt', 'mime': 'text/plain', 'can_read': True, 'can_write': True},
    'nwc': {'name': 'NoteWorthy Composer Binary', 'ext': 'nwc', 'mime': 'application/octet-stream', 'can_read': True, 'can_write': False},
    'humdrum': {'name': 'Humdrum', 'ext': 'krn', 'mime': 'text/plain', 'can_read': True, 'can_write': True},
    'krn': {'name': 'Humdrum', 'ext': 'krn', 'mime': 'text/plain', 'can_read': True, 'can_write': True},
    'romantext': {'name': 'Roman Numeral Text', 'ext': 'rntxt', 'mime': 'text/plain', 'can_read': True, 'can_write': True},
    'rntxt': {'name': 'Roman Numeral Text', 'ext': 'rntxt', 'mime': 'text/plain', 'can_read': True, 'can_write': True},
    'scala': {'name': 'Scala', 'ext': 'scala', 'mime': 'text/plain', 'can_read': True, 'can_write': True},
    'musedata': {'name': 'MuseData', 'ext': 'musedata', 'mime': 'text/plain', 'can_read': True, 'can_write': True},
    'mus': {'name': 'MuseData', 'ext': 'mus', 'mime': 'text/plain', 'can_read': True, 'can_write': False},
    'braille': {'name': 'Braille', 'ext': 'txt', 'mime': 'text/plain', 'can_read': False, 'can_write': True},
}

@app.route('/supported-formats', methods=['GET'])
def get_supported_formats():
    """Get list of all supported music file formats."""
    # Return a clean list without duplicates
    seen = set()
    formats = []
    for ext, info in FORMAT_INFO.items():
        if info['name'] not in seen:
            seen.add(info['name'])
            formats.append({
                'name': info['name'],
                'extensions': [e for e, i in FORMAT_INFO.items() if i['name'] == info['name']],
                'can_read': info['can_read'],
                'can_write': info['can_write'],
                'mime': info['mime']
            })
    return jsonify({'formats': formats})

@app.route('/upload-and-convert', methods=['POST'])
def upload_and_convert():
    """Upload a music file and convert to target format."""
    try:
        import tempfile
        import music21
        
        # Check if we have a file or JSON content
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400
            
            # Get file extension for format detection
            file_ext = os.path.splitext(file.filename)[1].lower().lstrip('.')
            target_format = request.form.get('format', 'musicxml')
            
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(mode='wb', suffix=f'.{file_ext}', delete=False) as temp_in:
                file.save(temp_in)
                temp_in_path = temp_in.name
        else:
            # Content via JSON
            data = request.json
            content = data.get('content')
            source_format = data.get('source_format')
            target_format = data.get('format', 'musicxml')
            
            if not content:
                return jsonify({'error': 'No content provided'}), 400
            if not source_format:
                return jsonify({'error': 'No source format specified'}), 400
            
            # Save content temporarily
            file_ext = source_format
            with tempfile.NamedTemporaryFile(mode='w+' if source_format in ['abc', 'musicxml', 'lilypond', 'mei', 'humdrum', 'romantext', 'scala', 'musedata', 'noteworthy', 'braille'] else 'wb', 
                                         suffix=f'.{file_ext}', delete=False, encoding='utf-8') as temp_in:
                temp_in.write(content)
                temp_in_path = temp_in.name
        
        try:
            # Parse the input file with music21
            score = music21.converter.parse(temp_in_path)
            
            # Create output file
            with tempfile.NamedTemporaryFile(mode='wb', suffix=f'.{FORMAT_INFO.get(target_format, {}).get("ext", target_format)}', delete=False) as temp_out:
                temp_out_path = temp_out.name
            
            # Special case: ABC+ needs preprocessing if it's the source
            if file_ext == 'abc' and target_format in ['musicxml', 'midi', 'lilypond']:
                # If we're converting from ABC, check if it's ABC+ and use our specialized tools
                try:
                    with open(temp_in_path, 'r', encoding='utf-8') as f:
                        abc_content = f.read()
                    
                    # Check if we should use our existing converters for ABC
                    if target_format == 'musicxml':
                        # Use existing convert endpoint logic
                        processed_abc = preprocess_abc(abc_content)
                        
                        with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False, encoding='utf-8') as temp_abc_processed:
                            temp_abc_processed.write(processed_abc)
                            temp_abc_processed_path = temp_abc_processed.name
                        
                        try:
                            result = subprocess.run(
                                [sys.executable, CONVERTER_SCRIPT, temp_abc_processed_path],
                                capture_output=True,
                                text=True,
                                encoding='utf-8',
                                check=False
                            )
                            
                            if result.returncode == 0:
                                with open(temp_out_path, 'w', encoding='utf-8') as f:
                                    f.write(result.stdout)
                            else:
                                # Fall back to music21
                                score.write(target_format, temp_out_path)
                        finally:
                            if os.path.exists(temp_abc_processed_path):
                                os.remove(temp_abc_processed_path)
                    
                    elif target_format == 'midi':
                        # Use abc2midi
                        processed_abc = preprocess_abc(abc_content)
                        
                        with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False, encoding='utf-8') as temp_abc_processed:
                            temp_abc_processed.write(processed_abc)
                            temp_abc_processed_path = temp_abc_processed.name
                        
                        try:
                            result = subprocess.run(
                                ['abc2midi', temp_abc_processed_path, '-o', temp_out_path],
                                capture_output=True,
                                text=True,
                                encoding='utf-8',
                                check=False
                            )
                            
                            if result.returncode != 0 or not os.path.exists(temp_out_path):
                                # Fall back to music21
                                score.write(target_format, temp_out_path)
                        finally:
                            if os.path.exists(temp_abc_processed_path):
                                os.remove(temp_abc_processed_path)
                    
                    elif target_format == 'lilypond':
                        # Use abc2ly
                        processed_abc = preprocess_abc(abc_content)
                        
                        with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False, encoding='utf-8') as temp_abc_processed:
                            temp_abc_processed.write(processed_abc)
                            temp_abc_processed_path = temp_abc_processed.name
                        
                        try:
                            result = subprocess.run(
                                ['abc2ly', '-o', temp_out_path, temp_abc_processed_path],
                                capture_output=True,
                                text=True,
                                encoding='utf-8',
                                check=False
                            )
                            
                            if result.returncode != 0 or not os.path.exists(temp_out_path):
                                # Fall back to music21 (though it doesn't write LilyPond)
                                raise Exception("abc2ly failed and music21 can't write LilyPond")
                        finally:
                            if os.path.exists(temp_abc_processed_path):
                                os.remove(temp_abc_processed_path)
                    else:
                        # Use music21 for other formats
                        score.write(target_format, temp_out_path)
                except Exception as e:
                    print(f"Specialized converter failed, falling back to music21: {e}", file=sys.stderr)
                    # Fall back to music21
                    score.write(target_format, temp_out_path)
            else:
                # Use music21 for all other conversions
                score.write(target_format, temp_out_path)
            
            # Read the output file
            mode = 'rb'
            encoding = None
            if target_format in ['abc', 'musicxml', 'lilypond', 'mei', 'humdrum', 'romantext', 'scala', 'musedata', 'noteworthy', 'braille']:
                mode = 'r'
                encoding = 'utf-8'
            
            with open(temp_out_path, mode, encoding=encoding) as f:
                output_content = f.read()
            
            # Determine MIME type
            mime_type = FORMAT_INFO.get(target_format, {}).get('mime', 'application/octet-stream')
            file_ext = FORMAT_INFO.get(target_format, {}).get('ext', target_format)
            
            # Create response
            if mode == 'r':
                # Text format, return as JSON for display
                return jsonify({
                    'success': True,
                    'content': output_content,
                    'format': target_format,
                    'mime': mime_type
                })
            else:
                # Binary format, return as file download
                response = make_response(output_content)
                response.headers['Content-Type'] = mime_type
                response.headers['Content-Disposition'] = f'attachment; filename=converted.{file_ext}'
                return response
                
        finally:
            # Clean up
            if os.path.exists(temp_in_path):
                os.remove(temp_in_path)
            if 'temp_out_path' in locals() and os.path.exists(temp_out_path):
                os.remove(temp_out_path)
                
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def kill_stale_process(port):
    """Attempt to find and kill any process already using the specified port."""
    try:
        if sys.platform == 'win32':
            # Windows: use netstat to find PID and taskkill to terminate
            cmd = f'netstat -ano | findstr : {port}'
            output = subprocess.check_output(cmd, shell=True).decode()
            for line in output.splitlines():
                if f':{port}' in line and 'LISTENING' in line:
                    pid = line.strip().split()[-1]
                    if pid != '0':
                        print(f"Cleaning up stale process on port {port} (PID: {pid})...", file=sys.stderr)
                        subprocess.run(['taskkill', '/F', '/PID', pid], check=False)
        else:
            # macOS / Linux: use lsof and kill
            try:
                output = subprocess.check_output(['lsof', '-ti', f':{port}'], text=True).strip()
                if output:
                    pids = output.split('\n')
                    for pid in pids:
                        if pid and int(pid) != os.getpid():
                            print(f"Cleaning up stale process on port {port} (PID: {pid})...", file=sys.stderr)
                            subprocess.run(['kill', '-9', pid], check=False)
            except subprocess.CalledProcessError:
                # lsof returns exit code 1 if no process is found
                pass
    except Exception as e:
        print(f"Warning: Could not check/kill stale process: {e}", file=sys.stderr)

if __name__ == '__main__':
    import webbrowser
    import threading
    
    # Auto-open browser after a short delay
    def open_browser():
        webbrowser.open('http://127.0.0.1:5001')
    
    # Clean up any existing process on port 5001
    kill_stale_process(5001)
    
    threading.Timer(1.5, open_browser).start()
    
    # Run Flask (debug=False for production app)
    app.run(debug=False, port=5001, host='127.0.0.1')
