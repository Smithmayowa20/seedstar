# Userlist

Make an application which stores names and email addresses in a database (SQLite is fine). a) Has welcome page in http://localhost/ - this page has links to list and create functions b) Lists all stored names / email address in http://localhost/list c) Adds a name / email address to the database in http://localhost/add - should validate input and show errors

This is a django based application so please make sure you use correctly all of django infrastructure (form, template inheritance, ORM). Also make sure the app does not have major security problems: CSRF, XSS, SQL Injection.

#Installation
Go to this directory
cd seedstar/userlist

Then install all requirements with
the command_prompt commmand
=="pip install requirements.txt"

Then collect the static files with
the command_prompt command
=="pip manage.py collectstatic"

Then run the development server with
the command_prompt command
=="pip manage.py runserver"

To run app/test.py script type the command
=="pip manage.py test"
into the command_prompt
