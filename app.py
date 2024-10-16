import logging
from flask import Flask, render_template, send_from_directory
import os

# Create the Flask app
app = Flask(__name__,
            static_folder="scratch-gui/build/static",  # Point to the static directory in the build
            template_folder="scratch-gui/build")  # Use build for templates as well

# Suppress Flask's default logging
log = logging.getLogger('werkzeug')  # This is the default logger for Flask
log.setLevel(logging.ERROR)  # Set to ERROR to suppress INFO and DEBUG messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.static_folder, 'static'), filename)

@app.route('/<path:filename>')
def serve_build_files(filename):
    return send_from_directory(app.template_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)  # Set debug=False to disable debug output
