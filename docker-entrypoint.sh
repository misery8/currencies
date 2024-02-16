#!/bin/bash

echo "Create a static folder"
mkdir -p static

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate

echo "Starting server..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000