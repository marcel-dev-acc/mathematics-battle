#!/bin/sh
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec api python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec api python manage.py collectstatic --no-input --clear