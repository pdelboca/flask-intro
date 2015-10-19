# Improt Flask app from the flask module
from flask import Flask, render_template, request, redirect, url_for
# Create the application object
app = Flask(__name__)

# use decorators to link a function to an url
@app.route('/')
def home():
	return "Hello, World!"

@app.route('/welcome') # By defect Flask assumes GET
def welcome():
	return render_template("welcome.html")

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug = True)