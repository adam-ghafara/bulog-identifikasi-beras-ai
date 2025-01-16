import unittest
from app import app
from selenium import webdriver
import time
import os

# Code Coverage the app.py
class TestApp(unittest.TestCase):
    def setUp(self):
        # Run the app.py
        os.system('python app.py')
        time.sleep(15)
        # Open the browser
        webdriver_path = 'D:/chromedriver_win32/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=webdriver_path)
        self.driver.get('http://127.0.0.1:5000')
        time.sleep(7)
        # Press on the identify button
        self.driver.find_element_by_id('btn-identify').click()
        time.sleep(7)
        # Upload the image into the form
        self.driver.find_element_by_id('submit-images').send_keys(os.path.abspath('C:/Users/adamg/Downloads/rice-2380808_960_720.jpg'))
        time.sleep(5)
        # Start the identification
        self.driver.find_element_by_id('identification-start').click()
        time.sleep(10)

    def test_kondisi_beras(self):
        self.assertEqual(self.driver.find_element_by_id('kondisi-beras').text, 'Kondisi Beras: Full ( Broken (<=15%) )')

    def test_warna_beras(self):
        self.assertEqual(self.driver.find_element_by_id('warna-beras').text, 'Warna Beras: Putih')

    def test_kesimpulan_beras(self):
        self.assertEqual(self.driver.find_element_by_id('kesimpulan-beras').text, 'Ini adalah Beras Premium. Dapat diketahui dengan jumlah butir patah yang lebih sedikit ( Broken (<=15%) ) sehingga dapat dipastikan ini adalah beras premium.')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
