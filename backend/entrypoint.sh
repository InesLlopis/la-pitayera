#!/bin/sh
# UD3.2.h
set -e

echo "Aplicando migraciones de Django..."
python manage.py migrate --noinput

echo "Iniciando servidor Django..."
exec python manage.py runserver 0.0.0.0:8000
