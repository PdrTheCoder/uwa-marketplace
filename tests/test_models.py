# test_models.py
import unittest
from uwamkp.models import User
from werkzeug.security import generate_password_hash

class UserModelTestCase(unittest.TestCase):
    def test_password_verification(self):
        user = User(password=generate_password_hash('testpassword'))
        self.assertTrue(user.verify_password('testpassword'))
        self.assertFalse(user.verify_password('wrongpassword'))

if __name__ == '__main__':
    unittest.main()
