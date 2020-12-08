#!/bin/bash
echo "Apply database migrations"

rm -Rf ./apps/migrations/0001*.py

python ./manage.py makemigrations
python ./manage.py migrate

gunicorn demo.wsgi:application --bind 0.0.0.0:8000
