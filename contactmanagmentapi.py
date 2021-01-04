
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class Users(db.Model):
    username = db.Column(db.String(50), primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    contact = db.Column(db.String(50))

class Emailinfo(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(100))
    

@app.route('/<username>/<fname>/<lname>/<contact>')
def index(username, fname, lname, contact):
    user = Users(username=username, fname=fname, lname=lname, contact=contact)
    db.session.add(user)
    db.session.commit()

    return '<h1>Added New User detail!</h1>'

@app.route('/<username>/<req_type>')
def manipulate_data(username, req_type):
    if req_type=='search':
        user = Users.query.filter_by(username=username).first()
        if user:
            return f'<h1>The contact number of this username is: { user.contact}</h1>'
        else:
            return f'<h1>User not found </h1>'
    elif req_type=='delete':
        #print('in delete clause')
        Users.query.filter_by(username=username).delete()
        return f'<h1>This user --> {username} has been deleted</h1>'


@app.route('/<username>/<value>/<req_type>')
def get_update(username, value, req_type):
    if req_type=='update':    
        user =  Users.query.filter_by(username=username).update(dict(contact=value))
        db.session.commit()
        return f'<h1>The contact number has been updated </h1>'
    elif req_type=='email':
        #print('in email adding part:  ')
        user = Users.query.filter_by(username=username).first()
        if user:
            user = Emailinfo(username=username, email=value)
            db.session.add(user)
            db.session.commit()
            return f'<h1>The Email {value} information has been added  </h1>'
        else:
            return f'<h1>User not found please add user first   </h1>'

@app.route('/')
def get_alluser():
    #print('in retretrieve')
    det = []
    info = Users.query.all()
    for i in info:
        qu = Emailinfo.query.filter_by(username=i.username).first()
        if not qu:
            val = 'Not found'
        else:
            val = qu.email
        a = f'<h1>{i.username} {i.fname} {i.lname} {i.contact} {val} </h1>'
        det.append(a)
    #user = Users.query.filter_by(username=username).first()

    return f'<h1>Username Firsrname Lastname Contact Email \n {det}: </h1>'



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)