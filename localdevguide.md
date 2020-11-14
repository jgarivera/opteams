# Local development setup
This is a guide in setting up a local development environment for OpTeams.
This will install a virtual Python environment where its dependencies are installed.
The local development database engine is SQLite.

## Creating a virtual env

The setup is now making use of virtual environments since we are going to deploy to Heroku.

Install virtualenv: `pip install virtualenv`

Create an env folder within opteams: `virtualenv env`

After that, run virtual python: `env\Scripts\activate.bat` This will make you run in a virtual Python environment.
All the next commands will be ran under the virtual environment.

(env) `pip install -r requirements.txt`

This will install:
* django
* Whitenoise
* Psycopg2
* Gitignore
* Dj-database-url
* Dj-static
* Static3
* Gunicorn
* django-heroku
* stream-python

## Setting up the dummy environment

While still inside the virtual environment,

Migrate the database: (env) `python manage.py migrate --settings=opteams.settings.dev`

Fill database with dummy data (users, channels, keys, assignments): (env) `python loaddummy.py`

Login using these accounts:

* admin (can access admin dashboard) user: `admin` password: `admin`
* ss191 (regular and limited to basic app) user: `ss191` password: `supersecret`

## Run the development server

(env) `python runserver.py`

This is a shortcut to: (env) `python manage.py runserver --settings=opteams.settings.dev`