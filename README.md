# Creating a virtual env:

The setup is now making use of virtual environments since we are going to deploy to Heroku

Install virtualenv: `pip install virtualenv`
Create an env folder within opteams: `virtualenv env`

After that, run virtual python: `env\Scripts\activate.bat`

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

# Setting up the dummy environment

Migrate the database: `python manage.py migrate --settings=opteams.settings.dev`

Create an admin account: `python manage.py createsuperuser --settings=opteams.settings.dev`

Fill database with dummy data (channels, keys, assignments): `python loaddummy.py`

# Run the server

`python runserver.py`

This is a shortcut to: `python manage.py runserver --settings=opteams.settings.dev`