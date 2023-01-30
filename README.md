Create a Python application for a shuttle bus.

a. Add a passenger with full name, phone number, city name.
b. Get the list of all passengers.
c. Get only required passenger details.
d. Update any changes to a passenger details.
e. Delete a passenger and his details.

Use CRUD operation for this. You can use Postman tool for the API CRUD operation calls. After testing, commit the code to your own GitHub repo.

Solution-- 

Pre-requsite : Learning about postman tool for testing api operation calls, and creating a database and table in mysql. and about pythonflask framework.

we have requrimetns.txt file which has all the needed dependencies that need to be install as mentioned below.

we can use to install all dependencies at once.
       pip install -r requirements.txt 

Otherwise, we can install the packages individually using below command.

Required package Installations --  
                                    pip install flask
                                    pip install flask-mysql 
                                    pip install -U flask-cors

Steps involved :

1. Initaially I have used Flask and mysql and Cors framework for creating python application.

2. I have created the shuttlebus as database and passengerinfo as table in mysql database.

3. I have used CRUD opertion such as GET, POST, PUT and DELETE operation in python application for api creation.

4. I have used Postman tool for the API CURD operation calls.

Description of the python files:

App.py -- This is for importing the flask and cors framework.

config.py -- This is configuring the mysql database and importing mysql framework.

main.py -- This is main application code for creating api and connecting the mysql and for mysql query.
      
 Run app with  python main.py



