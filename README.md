# School-management-system-cum-tracing-disciplinary-issues-in-django
# Technical background of the system
1. Programming language – Python programming
2. Framework – Django 3
3. Frontend – Bootstrap 4.0
4. Database - PostgreSQL 


# Features of the system 
1. Add and Manage staff
2. Can download the data for office record annually
3. Add and Manage student
4. Can download the data for office record annually
5. Add Class teacher
6. Add courses offered in the school
7. Trace student Disciplinary issue
8. Trace merit certificate of the student
9. Export data in csv format


# Installation with the postgres database
If you are running a project in postgres sql, you should follow the following 9 steps:
1. Install python version 8 and later
2. Install django >>pip install django
3. Make sure to install all the dependency required to run the project. Example(>>pip install django-filter)
4. Install postgres and create a database "jcs_db"
5. Run >>python manage.py migrate
6. Run >>python manage.py makemigrations
7. Run >>python manage.py createsuperuser 
8. Run your server >>python manage.py runserver
9. Login with the username and password created in a superuser


# Installation without postgres database. Using default database i.e. SQLite
Follow the following steps if you want to run a project without installing postgres:
1. Install python version 8 and later
2. Install django >>pip install django
3. Make sure to install all the dependency required to run the project. Example(>>pip install django-filter)
4. Go to the folder "school management system" >> settings.py and replace the database connection
 
		 Remove this from settings.py files and 
		 ----------------------------------------
		 DATABASES = {
				'default': {
						'ENGINE': 'django.db.backends.postgresql',
						'NAME': 'jcs_db',
						'USER': 'postgres',
						'PASSWORD': 'admin',
						'HOST': 'localhost',
						'PORT': '5432',
					 }
				 }


			Replace with this
			--------------------------------------
			DATABASES = {
				'default': {
						'ENGINE': 'django.db.backends.sqlite3',
						'NAME': BASE_DIR / 'db.sqlite3',
					 }
				}
   
6. Save your settings.py file (CTRL + S)
7. Run >>python manage.py migrate
8. Run >>python manage.py makemigrations
9. Run >>python manage.py createsuperuser 
10. Run your server >>python manage.py runserver
11. Login with the username and password created in a superuser

# Watch video demonstration 
https://youtu.be/5h3ne2de2b4
