FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc 
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
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
