### WatchUsBuild-TeamDirectoryAppWithDjango
### Code for the Directory app built during the Watch Us Build screencast.

### 0. init git

	# fork https://github.com/codeschool/WatchUsBuild-TeamDirectoryAppWithDjango
	# make a new workspace in cloud9.io named 'team_directory_app' and cloned from 
	#    https://github.com/sdoro/WatchUsBuild-TeamDirectoryAppWithDjango and
	#    choosing 'blank' template.

### 1. build a virtual environment

	sudo pip install virtualenv
	virtualenv $HOME/.env
	source $HOME/.env/bin/activate
	cd Directory
	pip install -r requirements.txt

### 2. Create/Use a project

	# django-admin.py startproject Directory
	cd Directory
	./manage.py runserver $IP:$PORT
	# test browsing https://team-directory-app-sdoro.c9users.io/

### 3. Create/use databases

	# edit Directory/settings.py
	# ./manage.py startapp www
	# edit www/models.py
	./manage.py makemigrations
	./manage.py migrate
	./manage.py createsuperuser
	# set email/password to ubu@c9.io/1617qwerty

### 4. Create/use an app

	# edit www/views.py
	# edit www/templates/index.html
	# edit Directory/urls.py
	# edit www/ursl.py
	# edit www/admin.py

### 5. Create/use a 'style'

	# edit www/static/main.css
	# edit www/static/normalize.css
	# edit www/templates/index.html
	
### 6. Load data

	# edit www/fixtures/team.json
	# ./manage.py loaddata www/fixtures/team.json

### 7. use Heroku

	heroku login
	# edit $HOME/workspace/ProcFile
	# edit DIrectory/settings.py
	heroku create
	edit DIrectory/wsgi.py