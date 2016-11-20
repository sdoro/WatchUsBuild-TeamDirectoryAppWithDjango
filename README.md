### WatchUsBuild-TeamDirectoryAppWithDjango
### Code for the Directory app built during the Watch Us Build screencast.

### 0. init git

	# fork https://github.com/codeschool/WatchUsBuild-TeamDirectoryAppWithDjango
	# make a new workspace in cloud9.io named 'team_directory_app' and cloned from 
	#    https://github.com/sdoro/WatchUsBuild-TeamDirectoryAppWithDjango and
	#    choosing 'blank' template.

### 1. build a virtual environment

	sudo pip install virtualenv
	virtualenv ~/.env
	source ~/.env/bin/activate
	cd Directory
	pip install -r requirements.txt

