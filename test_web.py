from selenium import webdriver
import time
import os

# Open the browser
driver = webdriver.Chrome()
# Open the website
driver.get('http://www.google.com')
time.sleep(7)
driver.quit()