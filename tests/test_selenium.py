# test_selenium.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get('http://localhost:5000/auth/login')  
        email_field = self.driver.find_element(By.NAME, 'email')
        password_field = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.CLASS_NAME, 'btn-primary')

        email_field.send_keys('0000@student.uwa.edu.au')
        password_field.send_keys('testpassword')
        submit_button = self.driver.find_element(By.CLASS_NAME, 'btn-primary')


        assert 'Welcome' in self.driver.page_source

if __name__ == '__main__':
    unittest.main()
