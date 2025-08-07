FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies, clean up to reduce image size
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .
EXPOSE 8000

# Optional: Create non-root user for security
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser /app
USER appuser

# Start the application
CMD ["gunicorn", "bookcatalog.wsgi:application", "--bind", "0.0.0.0:8000"]
