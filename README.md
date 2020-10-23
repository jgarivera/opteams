# Commands


python runserver.py 

This is a shortcut to: python manage.py runserver --settings=opteams.settings.dev

# Creating a virtual env:

The setup is now making use of virtual environments

Install virtualenv: pip install virtualenv
Create an env folder within opteams: virtualenv env

After that, run virtual python:

env\Scripts\activate.bat

(env) pip install -r requirements.txt

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