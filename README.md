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

