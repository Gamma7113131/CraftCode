import logging
import os
from flask import Flask, render_template, send_from_directory

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create the Flask app
app = Flask(__name__,
            static_folder=os.path.join(current_directory, 'scratch-gui/build/static'),  # Relative static folder path
            template_folder=os.path.join(current_directory, 'scratch-gui/build'))  # Relative template folder path

# Suppress Flask's default logging
log = logging.getLogger('werkzeug')  # This is the default logger for Flask
log.setLevel(logging.ERROR)  # Set to ERROR to suppress INFO and DEBUG messages

@app.route('/')
def index():
    # Serve the index.html from the new path
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    # Serve static files from the relative static directory
    return send_from_directory(os.path.join(current_directory, 'scratch-gui/build/static'), filename)

@app.route('/<path:filename>')
def serve_build_files(filename):
    # Serve other files from the build directory
    return send_from_directory(os.path.join(current_directory, 'scratch-gui/build'), filename)

if __name__ == '__main__':
    # Run the Flask application without extra logging
    app.run(debug=False)  # Set debug=False to disable debug output
