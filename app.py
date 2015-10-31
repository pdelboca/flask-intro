# Improt Flask app from the flask module
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
import os # for app.config
#import sqlite3

# Create the application object
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
# Create the SQLAlachemy object
db = SQLAlchemy(app)
from models import * # needs to be imported after the DB creation


# login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

# use decorators to link a function to an url
@app.route('/')
@login_required
def home():
	posts = db.session.query(BlogPost).all()
	return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			session['logged_in'] = True
			flash('You have been logged in!')
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You have been logged out!')
	return redirect(url_for('welcome'))

#def connect_db():
#	return sqlite3.connect(app.database)

# start the server with the 'run()' method
if __name__ == '__main__':
	app.run()