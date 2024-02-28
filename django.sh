#!/bin/bash
echo "Creating Migrations..."
# python manage.py migrate api zero
# python manage.py migrate auth zero
# python manage.py migrate client zero
python manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Fake Data..."
python create_fakers.py
echo ====================================

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000