# Dockerfile
FROM python:3.11-slim

# Set work dir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings

# Collect static (jika diperlukan)
RUN python manage.py collectstatic --noinput

# Expose Gunicorn port
EXPOSE 8080

# Migrate database
RUN python manage.py migrate
RUN python load_games.py

# Run server
CMD exec gunicorn config.wsgi:application --bind :8080 --workers 3

