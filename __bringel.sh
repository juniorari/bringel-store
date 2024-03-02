#!/bin/bash
echo "Creating Migrations..."
# python manage.py migrate auth zero
# python manage.py migrate client zero
# python manage.py migrate product zero
python manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Fake Data..."
python create_fakers.py
python manage.py createsuperuser --username admin --email email@email.com
echo ====================================

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000