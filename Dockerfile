# Use an official Python runtime as a parent image
FROM python:3.12-slim as python-base

# Set the working directory
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js
RUN apt-get update && apt-get install -y nodejs npm

# Copy the rest of your application code
COPY . .

# Install Node.js dependencies
RUN npm install

# Build your Node.js application
RUN npm run build

# Expose the port Flask will run on
EXPOSE 8000

# Command to run your application
CMD ["python", "app.py"]
