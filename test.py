import unittest
from flask.ext.testing import TestCase
from flask.ext.login import current_user
from project import app, db
from project.models import User, BlogPost

class BaseTestCase(TestCase):
	"""A Base Test Case"""

	def create_app(self):
		app.config.from_object('config.TestConfig')
		return app

	def setUp(self):
		db.create_all()
		db.session.add(User("admin", "admin@admin.com", "admin"))
		db.session.add(BlogPost("Test Post", "This is a test. Only a test.", 1))
		db.session.commit()

	def tearDown(self):
		db.session.remove()
		db.drop_all()


class FlaskTestCase(BaseTestCase):

	# ensure that flask was set up correctly
	def test_index(self):
		response = self.client.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# Ensure main page requires login
	def test_main_page_requires_login(self):
		response = self.client.get('/', follow_redirects=True)
		self.assertTrue(b'Please log in to access this page.' in response.data)

	# Ensure that posts show up in the main page
	def test_posts_show_up(self):
		response = self.client.post(
			'/login',
			 data=dict(username='admin',password='admin'),
			 follow_redirects=True
		)
		self.assertTrue('This is a test. Only a test.' in response.data)

class UsersViewsTests(BaseTestCase):


	# ensure that the login page looks correcly
	def test_login_page_loads(self):
		response = self.client.get('/login', content_type='html/text')
		self.assertTrue(b'Please login' in response.data)

	# Ensure login behaves correclty given the correct credentials
	def test_correct_login(self):
		with self.client:
			response = self.client.post(
				'/login',
				 data=dict(username='admin',password='admin'),
				 follow_redirects=True
			)
			self.assertTrue(b'You were logged in.' in response.data)
			self.assertTrue(current_user.name == 'admin')
			self.assertTrue(current_user.is_active())

	# Ensure login behaves correclty given the incorrect credentials
	def test_incorrect_login(self):
		response = self.client.post(
			'/login',
			 data=dict(username='wrong',password='wrong'),
			 follow_redirects=True
		)
		self.assertTrue(b'Invalid Credentials. Please try again.' in response.data)

	# Ensure logout behaves correctly
	def test_logout(self):
		with self.client:
			self.client.post(
				'/login',
				data=dict(username='admin',password='admin'),
				follow_redirects=True
			)
			response = self.client.get('/logout', follow_redirects=True)
			self.assertTrue(b'You were logged out.' in response.data)

	# Ensure logout page requires login
	def test_logout_page_requires_login(self):
		response = self.client.get('/logout', follow_redirects=True)
		self.assertTrue(b'Please log in to access this page.' in response.data)


if __name__ == '__main__':
	unittest.main()