import os
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Path to the abc2xml converter script
CONVERTER_SCRIPT = os.path.join(os.path.dirname(__file__), 'abc2xml', 'abc2xml.py')

import sys
import json
import re

# Load annotation guide
GUIDE_PATH = os.path.join(os.path.dirname(__file__), 'annotationguide.json')
try:
    with open(GUIDE_PATH, 'r') as f:
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
    return render_template('index.html')

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
        
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.abc', delete=False) as temp_abc:
            temp_abc.write(abc_content)
            temp_abc_path = temp_abc.name

        try:
            # Run the converter
            # abc2xml writes to stdout by default if no output file specified?
            # Wait, usually `python abc2xml.py file.abc` prints to stdout.
            # But earlier usage was `> output.xml`.
            # So yes, capture stdout.
            
            result = subprocess.run(
                ['python3', CONVERTER_SCRIPT, temp_abc_path],
                capture_output=True,
                text=True,
                check=False # Don't raise exception immediately, we want to capture stderr
            )
            
            if result.returncode != 0:
                # Converter failed
                return jsonify({'error': result.stderr or 'Unknown error occurred'}), 500
            
            xml_output = result.stdout
            return jsonify({'xml_content': xml_output})
            
        finally:
            # Clean up temp file
            if os.path.exists(temp_abc_path):
                os.remove(temp_abc_path)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
