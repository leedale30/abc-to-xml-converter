import os
import subprocess
import warnings
import urllib.request
import urllib.error

# App version - keep in sync with setup.py CFBundleVersion
APP_VERSION = "1.2.2"
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
                
                if xml_mapping.get('element') == 'direction' and xml_mapping.get('type') == 'words':
                    # Convert to text annotation: "args_str" or specific formatting
                    # Let's just use the raw args string as the text for now, or formatted.
                    # Ideally we'd parse the attributes defined in JSON.
                    # For simplicity, let's treat the whole arg string as the text content
                    # unless we want to format it nicely.
                    # Example conversion: %%dir mood="happy" -> "mood='happy'"
                    # Replace inner double quotes with single quotes to avoid breaking ABC string syntax
                    safe_args = args_str.replace('"', "'")
                    new_line = f'"{name}: {safe_args}"'
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

if __name__ == '__main__':
    import webbrowser
    import threading
    
    # Auto-open browser after a short delay
    def open_browser():
        webbrowser.open('http://127.0.0.1:5001')
    
    threading.Timer(1.5, open_browser).start()
    
    # Run Flask (debug=False for production app)
    app.run(debug=False, port=5001, host='127.0.0.1')
