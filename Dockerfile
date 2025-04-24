# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files 
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5001

# Start the Flask application
CMD ["python", "app.py"]
