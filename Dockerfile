# Use the official Python image as the base
FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# Set the working directory in the container
WORKDIR /app

# Copy application files
COPY /app /app

# Install system dependencies
RUN pip install certifi
# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
