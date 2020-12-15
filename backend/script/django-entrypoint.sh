#!/bin/bash
echo "Apply database migrations"

rm -Rf ./backend/apps/migrations/0001*.py

cd backend/apps && python ../manage.py makemigrations users
cd ../ && python manage.py makemigrations 

python manage.py migrate

# gunicorn 실행 시 django project directory에서 실행해야함.
gunicorn main.wsgi:application --bind 0.0.0.0:8000
