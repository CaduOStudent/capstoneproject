FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the rest of the application
COPY . .

# Run the application
CMD ["gunicorn", "bookcatalog.wsgi:application", "--bind", "0.0.0.0:8000"]