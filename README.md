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
if using already existing db, you can use the pre-registered user with username : **glenc** and password :  **ostenatious**

from link 127.0.0.1:8000/admin
this is the admin portal where admin can have comprehensive view of information in the database.
currently if using already provided db :username is **glenc** and password is  **ostenatious**
this should give you access to admin portal.

 In this portal is where you are able to set user authority as to whether registered users of the app are just **operators** or a **logistics manager** in order to differentiate roles


Once in portal the link packaging will be presented which enables user to view, update, delete, perform manipulations on the items provided in dropdown options


Tools:
Django framework
Python Programming Language

code by: glenchiridza
 
