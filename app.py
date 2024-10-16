import logging
from flask import Flask, render_template, send_from_directory

# Create the Flask app
app = Flask(__name__,
            static_folder="D:/EchoScript -/scratch-gui/build/static",  # Point to the static directory in the build
            template_folder="D:/EchoScript -/scratch-gui/build")  # Use build for templates as well

# Suppress Flask's default logging
log = logging.getLogger('werkzeug')  # This is the default logger for Flask
log.setLevel(logging.ERROR)  # Set to ERROR to suppress INFO and DEBUG messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory("D:/EchoScript -/scratch-gui/build/static", filename)

@app.route('/<path:filename>')
def serve_build_files(filename):
    return send_from_directory("D:/EchoScript -/scratch-gui/build", filename)

if __name__ == '__main__':
    # Run the Flask application without extra logging
    app.run(debug=False)  # Set debug=False to disable debug output
