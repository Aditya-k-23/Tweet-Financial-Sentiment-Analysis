# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY app.py requirements.txt ./
COPY saved_model ./saved_model

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]