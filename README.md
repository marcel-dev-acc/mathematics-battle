# Mathematics Battle
## Introduction
This is a small application that allows two users to compete head to head 
against each other in a mathematics challenge. Winner takes all! This project is
incomplete and would benefit from adding items in the "nice-to-have" section.

## Requirements: Ubuntu 20.04
1) Docker version 20.10.6, build 370c289 (you can use the docker engine install page [here](https://docs.docker.com/engine/install/ubuntu/)
to download the appropriate version for you computer) & docker-compose version 1.29.0, build 07737305 (you can use the compose install page [here](https://docs.docker.com/compose/install/) to get the stable version of docker-compose)
2) Clone this repository
3) Navigate to the root of the directory
4) Make sure the following files are executable:
    - start_deploy.sh
    - stop_deploy.sh
    - start_deploy_prod.sh
    - start_deploy_prod.sh
* This can be achieved by running `chmod +x "path_to_file/file"`

## Requirements: Mac OS
1) Docker latest (you can use the getting started page [here](https://docs.docker.com/get-started/)
to download the appropriate version for you computer)
2) Clone this repository
3) Navigate to the root of the directory
4) Make sure the following files are executable:
    - start_deploy.sh
    - stop_deploy.sh
    - start_deploy_prod.sh
    - start_deploy_prod.sh
* This can be achieved by running `chmod +x "path_to_file/file"`


## Launch
- Development: `./start_deploy.sh`
- Production: `./start_deploy_prod.sh`

If there are any migration errors then please follow this logic:
RUN
1) `./start_deploy.sh`
2) `./stop_deploy.sh`
3) `./start_deploy_prod.sh`
4) `./stop_deploy_prod.sh`
5) `./start_deploy_prod.sh`

It should now be working perfectly!

It is recommended that the line `.env*` is added to the .gitignore once you have cloned this project.
For the purposes of this project they have been left in as a point of reference.


## Creating new applications in Django
Once your development environment is up and running you can add "apps" to django by 
running the following commands:

For the API:

`docker-compose exec api python manage.py startapp <application name>`

For the UI:

`docker-compose exec ui python manage.py startapp <application name>`


## Development end-points
API:

http://localhost:3011/upload

http://localhost:3011/admin

http://localhost:3011/api/status

http://localhost:3011/api/create_session

http://localhost:3011/api/sessions

http://localhost:3011/api/session/<str:session_id>/user

http://localhost:3011/api/session/<str:session_id>/user/<str:username>/problem

http://localhost:3011/api/session/<str:session_id>/user/<str:username>/solution


## Production end-points
http://localhost:1350/upload

http://localhost:1350/api/status

http://localhost:1350/api/create_session

http://localhost:1350/api/sessions

http://localhost:1350/api/session/<str:session_id>/user

http://localhost:1350/api/session/<str:session_id>/user/<str:username>/problem

http://localhost:1350/api/session/<str:session_id>/user/<str:username>/solution


## API Documentation
All calls return a response code as defined by the standard https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

This is a standard json payload API
```
GET Request > /api/status

POST > /api/create_session
Response payload:
{
    'status': String,
    'message': String,
    'data': {
        'session_id': String,
    }, 
}

GET > /api/sessions
Response payload:
{
    'status': String,
    'message': String,
    'data': {
        'session_id': String,
        'players': List,
    },
}

PUT > /api/session/<str:session_id>/user
Request payload:
{
    'username': String
}
Response payload:
{
    'status': String,
    'message': String
}

GET > /api/session/<str:session_id>/user/<str:username>/problem
Response payload:
{
    'status': String,
    'message': String,
    'data': {
        'question_id': Integer,
        'problem': String,
    }
}

POST > /api/session/<str:session_id>/user/<str:username>/solution
Request payload:
{
    'problem_id': Integer,
    'answer': String
}
Response payload:
{
    'status': String,
    'message': String
}
```


## Setup (attribution)
The initial setup of the project is created by using the following guide:
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/


## Technologies
The setup of the project is close to production ready and uses 
the following technologies:
1) Docker
2) Django
3) Postgres
4) Gunicorn
5) Nginx


## User Story
As a part-time tutor I sometimes get asked if there are resources out there that are engaging for younger mathematics students.
I have previously built basic calculators for students to access online if they had "forgotten" their calculators at home. I wondered if
it was possible to build a proto-type of a platform that would use the idea of code-calculators to generate and present students
with mathematics problems that they could solve. These problems could range in difficulty from easy to difficult, with easy being basic mathematics problems with numbers between 1 and 100, and difficult being as tricky as solving algebraic expressions.

This proto-type will display the possibility of building such a platform by showcasing a head to head competition between two players
solving basic mathematics problems. Future development should focus on completing the objectives of the wire-frames included herein.


### Wire-frames
Web browser session page

![index web](documentation-assets/wireframe-images/index.html-web.png)

Mobile browser session page

![index mobile](documentation-assets/wireframe-images/index.html-mobile.png)

Web browser add user to game

![add user web](documentation-assets/wireframe-images/game.html-adduser.png)

Mobile add user to game

![add user mobile](documentation-assets/wireframe-images/game.html-adduser-mobile.png)

Web browser mark user ready

![mark user ready web](documentation-assets/wireframe-images/game.html-markready-web.png)

Mobile mark user as ready

![mark user ready mobile](documentation-assets/wireframe-images/game.html-markready-mobile.png)

Web browser countdown to game start

![game countdown web](documentation-assets/wireframe-images/game.html-3,2,1...-web.png)

Web browser game screen

![game screen web](documentation-assets/wireframe-images/game.html-player1&2screen.png)

Mobile game screen

![game screen mobile](documentation-assets/wireframe-images/game.html-player1screen-mobile.png)


### Website showcase
Session main page

![session page 1](documentation-assets/showcase-images/session_page_1.png)

Session page with a created session

![session page 2](documentation-assets/showcase-images/session_page_2_new_session.png)

Game page add a user

![game page 1](documentation-assets/showcase-images/game_page_1_add_user_form.png)

Game page user added to input

![game page 2](documentation-assets/showcase-images/game_page_2_add_user_inputed.png)

Game page user 1 waiting for another player

![game page 3](documentation-assets/showcase-images/game_page_3_user_1_waiting.png)

Second user on the sessions selection page

![session page 3](documentation-assets/showcase-images/session_page_3_user_2.png)

Second user on game page add user

![game page 4](documentation-assets/showcase-images/game_page_4_second_user_input.png)

Second user on game page input username

![game page 5](documentation-assets/showcase-images/game_page_5_second_user_input_name.png)

Both users on game page ready to play

![game page 6](documentation-assets/showcase-images/game_page_6_both_users_ready.png)

Game page user 1 generate their first problem

![game page 7](documentation-assets/showcase-images/game_page_7_user_1_generate_problem.png)

Game page user 2 generates their first problem

![game page 8](documentation-assets/showcase-images/game_page_8_user_2_generates_problem.png)

Game page user 1 enters a solution

![game page 9](documentation-assets/showcase-images/game_page_9_user_1_enters_answer.png)

Game page, showing that both pages continue to maintain sync

![game page 10](documentation-assets/showcase-images/game_page_x10_both_pages_sync.png)

Game page with an additional observer

![game page 11](documentation-assets/showcase-images/game_page_x11_with_observer.png)


## User Documentation
Navigate to the website url `http://localhost:3010/` or `http://localhost:1340/` click on create a session, this will add a session in the card below.
When you are ready, click on the session link. Duplicate your current browser to simulate another user.
At this point both browser windows should be asking for a username and to select the difficulty. Enter a
valid username in each of the windows and submit.

Begin playing the game by clicking on the generate problem button in each of the windows. As the game continues
you will see that both browser windows will stay in sync with each other, displaying both your score and the competitors
as problems get solved.

Submitting a solution doesn't guarantee that a point will be added, only when the solution is correct will a user obtain
a point. Likewise, the user has the option to skip a problem and generate another to solve if it is to difficult.

Opening another browser window will allow you to simulate a third user viewing the game as it goes on.


## Nice-to-have
This project would benefit from the following:

### API
1) Swagger API documentation
2) Basic logging is included, this should be changed to logging via a url webhook (i.e. Slack)

### UI
1) A progress bar that denotes the amount of time remaining until a winner is decided
2) A time counter that defines how many seconds / minutes are left until the game ends
3) A session management / user management page
4) Add scope for additional players at the same time (This way there could be an infinite amount of players)