#!/bin/bash

# Navigate to the scratch-gui directory, install dependencies, and build the project
cd scratch-gui
npm install    # Install Node.js dependencies
npm run build  # Build the Node.js application

# Start the Flask application in the background
cd ..          # Navigate back to the root directory
python app.py &  # Start Flask in the background

# Optionally, you can add a command to start the Node.js server here if needed
# If you need to run a Node.js server, use this line:
# node path/to/your/node/server.js
