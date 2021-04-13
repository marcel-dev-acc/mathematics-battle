#!/bin/sh
BASE_DIR="$( cd  "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec api python manage.py makemigrations --noinput
docker-compose -f docker-compose.prod.yml exec api python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec api python manage.py collectstatic --no-input --clear

echo "Sleeping for 5 seconds"
sleep 5

pytest $BASE_DIR/cli/api_prod.py