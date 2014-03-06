
# A very simple Flask Hello World app for you to get started with...

from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Email
from flask import Flask, request
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rtrajano:pybulls@mysql.server/rtrajano$pybulls1'
db = SQLAlchemy(app)


#app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'mysecretkey'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def hello_world():
    return 'Hello from Flask yayayayaya!'

class MyForm(Form):
    name = TextField('name', validators=[DataRequired()])
    email = TextField('email', validators=[DataRequired(), Email(message=u'Invalid email address.')])

@app.route('/user/username')
def show_user_profile():
    # show the user profile for that user
    user = request.args.get('username')
    return 'User %s' % user

@app.route('/success', methods=('GET', 'POST'))
def success():
    return "WTF!"

@app.route('/userhandler', methods=('GET', 'POST'))
def userhandler():
    return "WTF!"

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return "we posted right"
    #return render_template(r'C:\Users\ddye\Documents\PyBulls\teach-me-flask\templates\submit.html', form=form)
    #return render_template(r'C:\Users\ddye\Documents\PyBulls\teach-me-flask\templates\submit.html')
    #return render_template('submit.html')
    #return "Hello!"
    return render_template('submit.html', form=form)