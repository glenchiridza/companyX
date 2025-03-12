#Company X Automation process
### This aims to automate process of loading packages, into pallets, lines, racks into a warehouse 

### To run App type command
python manage.py runserver

### To install any missing requirements that may be required in app type command
pip install -r requirements.txt

### To add more models, after altering, youshould make migrations with the commands
python manage.py makemigrations
then
python manage.py migrate

### App running on localhost, after typing and click enter on the run commmand
should see link : 127.0.0.1:8000/
this will take you to home page where you access authentication links and app landing paging
user/ operator must register before being able to access the system that allows the automation of processes as assigned in document
if using already existing db, you can use the pre-registered user with username : **glenc** and password :  **ostentatious$97**

from link 127.0.0.1:8000/admin
this is the admin portal where admin can have comprehensive view of information in the database.
currently if using already provided db :username is **glenc** and password is  **ostentatious$97**
this should give you access to admin portal.

 In this portal is where you are able to set user authority as to whether registered users of the app are just **operators** or a **logistics manager** in order to differentiate roles


Once in portal the link packaging will be presented which enables user to view, update, delete, perform manipulations on the items provided in dropdown options



#### Additional Commands:
To createsuper user from terminal if starting with new DB: python manage.py shell
this will bring up a shell where you must import the user model from the user package and set the needed field values like username, password,is_staff,is_superuser, email,etc (just check fields presented in User model)

once objet is saved you should exit shell and type in terminal : python manage.py changepassword
this command will let you set a hashed password for the new admin account


Tools:
Django framework
Python Programming Language

code by: glenchiridza
 
