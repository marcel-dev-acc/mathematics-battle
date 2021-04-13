#!/bin/sh
BASE_DIR="$( cd  "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

docker-compose up -d --build

echo "Sleeping for 5 seconds"
sleep 5

pytest $BASE_DIR/cli/api.py