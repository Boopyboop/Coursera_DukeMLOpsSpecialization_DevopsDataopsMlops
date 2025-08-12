# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy only requirements and install first for cache efficiency
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt

# Copy project code
COPY . /app

# Ensure models directory exists (pipeline will drop artifacts here)
RUN mkdir -p /app/models

ENV MODEL_PATH=/app/models/model.joblib
EXPOSE 8000

# Use gunicorn for production-like run
CMD ["gunicorn", "service.app:app", "-b", "0.0.0.0:8000", "--workers", "2", "--threads", "4"]
