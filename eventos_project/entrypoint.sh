#!/bin/bash

# Salir del script si ocurre algún error
set -e

# Ejecutar migraciones de base de datos
echo "Aplicando migraciones..."
python manage.py makemigrations
python manage.py migrate

# Iniciar Gunicorn
echo "Iniciando Gunicorn..."
exec "$@"
