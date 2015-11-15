###############
### imports ###
###############

from project import app, db
from project.models import BlogPost
from flask import flash, redirect, render_template, url_for, session, Blueprint
from flask.ext.login import login_required
from functools import wraps

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

################
#### routes ####
################

# use decorators to link a function to an url
@home_blueprint.route('/')
@login_required
def home():
	posts = db.session.query(BlogPost).all()
	return render_template('index.html', posts=posts)

@home_blueprint.route('/welcome')
def welcome():
	return render_template('welcome.html')
