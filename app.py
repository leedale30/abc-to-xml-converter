import os
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Path to the abc2xml converter script
CONVERTER_SCRIPT = os.path.join(os.path.dirname(__file__), 'abc2xml', 'abc2xml.py')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        abc_content = request.json.get('abc_content')
        if not abc_content:
            return jsonify({'error': 'No content provided'}), 400

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
