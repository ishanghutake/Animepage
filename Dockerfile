# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code into the container
COPY . .

# Set the environment variable for Flask to listen on all interfaces
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the desired port
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--port=3000"]