#!/bin/bash

echo "Create a static folder"
mkdir -p static

echo "Collect static files"
python app/manage.py collectstatic --noinput

echo "Apply database migrations"
python app/manage.py migrate

echo "Starting server..."
gunicorn --config gunicorn-cfg.py app.config.wsgi:application