###############
### imports ###
###############

from flask import Flask, flash, redirect, render_template, url_for, session
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
import os # for app.config

################
#### config ####
################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import * # needs to be imported after the DB creation
from project.users.views import users_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)


##########################
#### helper functions ####
##########################

def login_required(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('users.login'))
	return wrap


################
#### routes ####
################

# use decorators to link a function to an url
@app.route('/')
@login_required
def home():
	posts = db.session.query(BlogPost).all()
	return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')


####################
#### run server ####
####################

# start the server with the 'run()' method
if __name__ == '__main__':
	app.run()