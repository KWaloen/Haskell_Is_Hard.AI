# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app/

# Expose the Gunicorn port
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "haskellishardai_backend.wsgi:application", "--bind", "0.0.0.0:8000"]