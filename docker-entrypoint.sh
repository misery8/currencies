#!/bin/bash

echo "Collect static files"
python app/manage.py collectstatic --noinput

python app/manage.py migrate

echo "Starting server..."
gunicorn --config gunicorn-cfg.py app.config.wsgi:application