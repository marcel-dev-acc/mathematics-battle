# mathematics-battle
This is a small application that allows two users to compete head to head 
against each other in a mathematics challenge. Winner takes all!

## Requirements
1) Docker 3.1.0 (you can use the getting started page here[https://docs.docker.com/get-started/] 
to download the appropriate version fro you computer)
2) Clone this repository
3) Navigate too to the root of the directory
4) Make sure the following files are executable:
    - start_deploy.sh
    - stop_deploy.sh
    - start_deploy_prod.sh
    - start_deploy_prod.sh
* This can be achieved by running `chmod +x "path_to_file/file"`
5) Run: `./start_deploy_prod.sh`

## Creating new applications in Django
docker-compose exec api python manage.py startapp <application name>
docker-compose exec ui python manage.py startapp <application name>

## Development end-points
http://localhost:3011/upload
http://localhost:3011/admin

## Production end-points
http://localhost:3011/upload

## Setup (attribution)
The initial setup of the project is created by using the following guide:
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

The setup of the project is close to production ready and uses 
the following technologies:
1) Docker
2) Django
3) Postgres
4) Gunicorn
5) Nginx

It is recommended that the line `.env*` is added to the .gitignore once you have cloned this project.
For the purposes of this project they have been left in as a point of reference.

Basic logging is included, this should be changed to logging via a url webhook (i.e. Slack)