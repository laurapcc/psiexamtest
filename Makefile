install_postgres:
	sudo systemctl restart postgresql

create_virtualenv:
	# en root
	python3.7 -m venv psienv
	# en la carpeta mia
	source ~/psienv/bin/activate
	pip3 install -r requirements.txt
	pip3 install gunicorn
	pip3 install whitenoise

	# deactivate



create_project:
	django-admin startproject proyecto

create_app:
	python3 manage.py startapp applicacion
# add app to settings.INSTALLED_APPS -> 'applicacion.apps.ApplicacionConfig'
# changes in settings.py:
#	import os, dj_database_url
#	DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
#	INSTALLED_APPS -> 'catalog.apps.CatalogConfig',
#	??? INSTALLED_APPS -> 'debug_toolbar'
#	TEMPLATES['DIRS']: [os.path.join(BASE_DIR, 'templates')]
#	DATABASES = {}
#	if os.getenv('SQLITE', False):
#	    DATABASES['default'] = {
#	        'ENGINE': 'django.db.backends.sqlite3',
#	        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#	    }
#	else:
#	    DATABASES['default'] = dj_database_url.config(
#	        default='postgres://alumnodb:alumnodb@localhost:5432/examen',
#	        conn_max_age=500)
#	TIME_ZONE = 'Europe/Madrid'

create_db:
	dropdb --if-exists -U alumnodb -h localhost examendb
	createdb -U alumnodb -h localhost examendb
	make migrations
	make create_super_user

create_super_user:
	python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('alumnodb', 'admin@myproject.com', 'alumnodb')"

server:
	python3 manage.py runserver 8001

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

populate:
	python3 manage.py popular

test:
	python3 manage.py test

otro:
	git config --global user.email "lauradepazc@gmail.com"
	git config --global user.name "laurapcc"

push:
	#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
	git add -A
	git commit -m "dfgh6"
	git push

heroku:
	heroku create
	git push heroku main
	heroku run python manage.py migrate
	heroku run python manage.py createsuperuser
