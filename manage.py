import os
import unittest
import coverage
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from project import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
	"""Runs the tests without coverage."""
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def cov():
	cov = coverage.coverage(branch=True, include="project/*")
	cov.start()
	tests = unittest.TestLoader().discover("tests")
	unittest.TextTestRunner(verbosity=2).run(tests)
	cov.stop()
	cov.save()
	print "Coverage Summary: "
	cov.report()
	base_dir = os.path.abspath(os.path.dirname(__file__))
	cov_dir = os.path.join(base_dir, 'coverage')
	cov.html_report(directory=cov_dir)
	cov.erase()	

if __name__ == '__main__':
	manager.run()