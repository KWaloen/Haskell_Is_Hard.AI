# Use an official Python runtime as a parent image
FROM python:3.12

# Copy and install dependencies
COPY requirements.txt /haskellishardai_backend/

# Set working directory
WORKDIR /haskellishardai_backend


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project
COPY . /haskellishardai_backend/

# Expose the Gunicorn port
EXPOSE 8000

# collect all static files to the root directory - mainly for admin panel
RUN python manage.py collectstatic --no-input

# migrate db
RUN python manage.py migrate
RUN python manage.py load_llm_data

# Run Gunicorn
CMD ["gunicorn", "haskellishardai_backend.wsgi:application", "--bind", "0.0.0.0:8000"]