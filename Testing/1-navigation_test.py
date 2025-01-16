import coverage
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Navigation Test
class NavigationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cov = coverage.Coverage()
        cls.cov.start()

    def setUp(self):
            # Start Browser
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            # Open the website
            self.driver.get('http://127.0.0.1:5000')
    
    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.cov.stop()
        cls.cov.save()
        cls.cov.report()
        cls.cov.html_report(directory='navigation_coverage_report')
        print("Coverage report generated in the 'navigation_coverage_report' directory.")

    def test_navigation(self):
        self.driver.find_element(By.ID, 'about-bar').click()
        time.sleep(7)

        self.driver.find_element(By.ID, 'index-button').click()
        time.sleep(7)

        self.driver.find_element(By.ID, 'identify-bar').click()
        time.sleep(7)

        self.driver.find_element(By.ID, 'index-button').click()
        time.sleep(7)

        self.driver.find_element(By.ID, 'about-footer').click()
        time.sleep(7)

        self.driver.find_element(By.ID, 'index-button').click()
        time.sleep(7)

        self.driver.find_element(By.ID, 'btn-identify').click()
        time.sleep(7)

        self.driver.find_element(By.ID, 'index-button').click()
        time.sleep(7)

        self.driver.find_element(By.ID, 'feedback-footer').click()
        time.sleep(7)

        self.driver.find_element(By.ID, 'index-button').click()
        time.sleep(7)

if __name__ == '__main__':
    unittest.main()