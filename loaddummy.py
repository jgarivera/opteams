import os
os.system("python manage.py loaddata core\\fixtures\\keys.json --settings=opteams.settings.dev")
os.system("python manage.py loaddata core\\fixtures\\channels.json --settings=opteams.settings.dev")
os.system("python manage.py loaddata core\\fixtures\\assignments.json --settings=opteams.settings.dev")
os.system("python manage.py loaddata core\\fixtures\\users.json --settings=opteams.settings.dev")