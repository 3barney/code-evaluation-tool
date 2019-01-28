#!/bin/sh

echo "Waiting for postgress..."

while ! nc -z users_db 5432; do
  sleep 0.1
done

echo "Postgress started"


python manage.py run -h 0.0.0.0