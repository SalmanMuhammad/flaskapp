# flaskapp
simple flask contact management api using sqlite and flask-sqlalchemy 

1.first install the requirement.txt
2.insall sqlite on you system for db
3. run this appilication 
4. copy the url and open in your browser http://127.0.0.1:5000/
 note* for creating the db and its table
	open command line and cd to current dir
	now open python 
		from contactmanagmentapi import db
		db.create_all()
 Run the application again	

Test Cases

5. Insert data using this line http://127.0.0.1:5000/username/Firstname/Lastname/contactno
	eg. http://127.0.0.1:5000/jhony123/jhony/dep/+96351-1234565
		note* username should be unique otherwise app will through error

6. insert data as much as you want by using the above example

7. for viewing the data that you already inserted open this in your browser http://127.0.0.1:5000/

8. lets search contact by using username http://127.0.0.1:5000/username/request_type
	eg. http://127.0.0.1:5000/jhony123/search

9. delete a contact by using username http://127.0.0.1:5000/username/request_type
	eg. http://127.0.0.1:5000/jhony12/delete

10. update contact by using http://127.0.0.1:5000/username/contactno/request_type
	eg. http://127.0.0.1:5000/jhony12/+93524-53651-5/update

11.lets add email for specific user http://127.0.0.1:5000/username/email/request_type
	eg. eg. http://127.0.0.1:5000/jhony12/jhony12@gmail.com/email
  for adding multiple emails
	eg. eg. http://127.0.0.1:5000/jhony12/jhony12@gmail.com, jhony12@hotmail.com/email

12. for viewing the data that you already inserted open this in your browser http://127.0.0.1:5000/
