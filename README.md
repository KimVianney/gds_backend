# GDS Backend

## Getting Started

- Create a virtual environment `python3 -m venv venv`

- Activate the virtual environment `. venv/bin/activate`

- Install all dependencies `pip install -r requirements.txt`

- Create a `.env` file and add the variables from `.env_example`

- Source the environment variables `source .env`

- Make databse migrations `python manage.py migrate`

- Run the server `python manage.py runserver`

## Deploying To Compute Engine

**ENSURE TO CREATE A NEW USER FOR YOUR SYSTEM, DONT WORK ON THE ROOT USER**

- Clone this repo to your instance 

- Install dependencies to be used by your instance, such as postgresql, nginx etc

- Switch to the backend directory `cd raid_be`

- Create a virtual environment `python3 -m venv venv` and activate it `. venv/bin/activate`

- Install dependencies `pip install -r requirements.txt`

- Create a `.env` file and add the required environment variables from `.env_example`

  - `touch .env`

  - `cp .env_example .env`

  - `nano .env` to edit the values

  - `source .env` to add them to the session

- Make database migrations `python manage.py migrate`

- Create static files `python manage.py collectstatic`

- To run the server:

  - **THIS MUST BE DONE IN 2 DIFFERENT TERMINAL SESSIONS WITH THE SAME SUDO USER**

  - For Django App:

    - Create a new terminal session and login as `gds` with `su - gds`

    - Switch to the backend directory `cd gds_backend`

    - Activate the virtual environment `. venv/bin/activate`

    - Source environment variables `source .env`

    - Run server `gunicorn api.wsgi -b 0.0.0.0:8080 --timeout 900 --log-level debug --log-file -`

  - For Start Celery service:

    - Create a new terminal session and login as `gds` with `su - gds`

    - Switch to the backend directory `cd gds_backend`

    - Activate the virtual environment `. venv/bin/activate`

    - Source environment variables `source .env`

    - Start celery `celery -A api worker -l info`