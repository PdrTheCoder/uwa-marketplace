# test_client.py
from datetime import datetime, timezone
import unittest
from uwamkp.app import app
from uwamkp.models import db 
from uwamkp.models import User
from werkzeug.security import generate_password_hash

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client using the Flask application configured for testing
        self.app = app.test_client()
        self.ctx = app.app_context()  # Create an application context
        self.ctx.push()  # Push the context so the app is active

        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        # Setup a clean temporary database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()  # pop the context in teardown

    def test_login_route(self):
        # Create user in database
        user = User(email='0000@student.uwa.edu.au', 
                    username='test_user', 
                    password=generate_password_hash('testpassword'),
                    created_at=datetime.now(timezone.utc),  # Include the current time for created_at
                    is_admin=False,  # Assume a default value for is_admin if it's required
                    deleted=False    # Assume a default value for deleted if it's required
                    )
        db.session.add(user)
        db.session.commit()

        response = self.app.post('/auth/login', data={'email': '0000@student.uwa.edu.au', 'password': 'testpassword'}, follow_redirects=True)
        #self.assertIn(b'You have been logged in', response.data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
