import coverage
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class IdentifyTest(unittest.TestCase):
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
            time.sleep(5)
    
    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.cov.stop()
        cls.cov.save()
        cls.cov.report()
        cls.cov.html_report(directory='identify_coverage_report')
        print("Coverage report generated in the 'identify_coverage_report' directory.")

    def test_identify(self):

        # Press on the identify button
        self.driver.find_element(By.ID, 'btn-identify').click()
        time.sleep(7)
        
        # Upload the image into the form
        self.driver.find_element(By.ID, 'dropzone-file').send_keys(os.path.abspath('C:/Users/adamg/Desktop/AI AND DATASET/Rice Model/Test Samples/Sample (1).jpg'))
        time.sleep(5)
        
        # Start the identification
        self.driver.find_element(By.ID, 'identification-start').click()
        time.sleep(10)
        
        # Check if the result is displayed

        self.assertEqual(self.driver.find_element(
          By.ID, 'image-display').is_displayed(), True
        )

        self.assertEqual(self.driver.find_element(
          By.ID, 'kondisi-beras').is_displayed(), True
        )
        
        self.assertEqual(self.driver.find_element(
          By.ID, 'kondisi-beras').is_displayed(), True
        )
        self.assertEqual(self.driver.find_element(
          By.ID, 'warna-beras').is_displayed(), True
        )
        self.assertEqual(self.driver.find_element(
          By.ID, 'kesimpulan-beras').is_displayed(), True
        )
        self.assertEqual(self.driver.find_element(
          By.ID, 'acccuracy-display').is_displayed(), True
        )
        time.sleep(5)

        # Second test
        self.driver.find_element(By.ID, 'identify-re').click()
        time.sleep(7)

        self.driver.find_element(By.ID, 'dropzone-file').send_keys(os.path.abspath('C:/Users/adamg/Desktop/AI AND DATASET/Rice Model/Test Samples/Gambar WhatsApp 2025-01-09 pukul 20.47.18_433dfa5d.jpg'))
        time.sleep(5)

        self.driver.find_element(By.ID, 'identification-start').click()
        time.sleep(10)
    
        self.assertEqual(self.driver.find_element(
          By.ID, 'kondisi-beras').is_displayed(), True
        )
        self.assertEqual(self.driver.find_element(
          By.ID, 'warna-beras').is_displayed(), True
        )
        self.assertEqual(self.driver.find_element(
          By.ID, 'kesimpulan-beras').is_displayed(), True
        )
        self.assertEqual(self.driver.find_element(
          By.ID, 'accuracy-display').is_displayed(), True
        )
        time.sleep(5)

        # Third test
        self.driver.find_element(By.ID, 'identify-re').click()

        self.driver.find_element(By.ID, 'dropzone-file').send_keys(os.path.abspath('C:/Users/adamg/Desktop/AI AND DATASET/Rice Model/Test Samples/Gambar WhatsApp 2025-01-09 pukul 20.47.18_433dfa5d.jpg'))
        time.sleep(5)
        
        self.driver.find_element(By.ID, 'identification-start').click()
        time.sleep(10)
        
        self.assertEqual(self.driver.find_element(By.ID, 'kondisi-beras').is_displayed(), True)
        self.assertEqual(self.driver.find_element(By.ID, 'warna-beras').is_displayed(), True)
        self.assertEqual(self.driver.find_element(By.ID, 'kesimpulan-beras').is_displayed(), True)
        self.assertEqual(self.driver.find_element(By.ID, 'accuracy-display').is_displayed(), True)
        time.sleep(5)
        
        self.driver.find_element(By.ID, 'index-button').click()
        time.sleep(7) 
    
if __name__ == '__main__':
     unittest.main()