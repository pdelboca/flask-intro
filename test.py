from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

	# ensure that flask was set up correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# ensure that the login page looks correcly
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Please login' in response.data)

	# Ensure login behaves correclty given the correct credentials
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			 data=dict(username='admin',password='admin'),
			 follow_redirects=True
		)
		self.assertTrue(b'You have been logged in!' in response.data)

	# Ensure login behaves correclty given the incorrect credentials
	def test_incorrect_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			 data=dict(username='wrong',password='wrong'),
			 follow_redirects=True
		)
		self.assertTrue(b'Invalid credentials. Please try again.' in response.data)

	# Ensure logout behaves correctly
	def test_logout(self):
		tester = app.test_client(self)
		tester.post(
			'/login',
			data=dict(username='admin',password='admin'),
			follow_redirects=True
		)
		response = tester.get('/logout', follow_redirects=True)
		self.assertTrue(b'You have been logged out!' in response.data)

	# Ensure main page requires login
	def test_main_page_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects=True)
		self.assertTrue(b'You need to login first.' in response.data)

	# Ensure logout page requires login
	def test_main_page_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/logout', follow_redirects=True)
		self.assertTrue(b'You need to login first.' in response.data)

	# Ensure that posts show up in the main page
	def test_posts_show_up(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			 data=dict(username='admin',password='admin'),
			 follow_redirects=True
		)
		self.assertTrue('Hello from the shell' in response.data)


if __name__ == '__main__':
	unittest.main()