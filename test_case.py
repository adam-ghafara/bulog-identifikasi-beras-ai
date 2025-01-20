import pytest
import coverage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app import app
import os
import time

os.environ['COVERAGE_PROCESS_START'] = '.coveragerc'

# Selenium browser fixture
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://127.0.0.1:5000')
    yield driver
    driver.quit()

# Helper function to upload a file and check results
def upload_and_check_results(driver, file_path):
    # Upload file and check results
    time.sleep(5)
    driver.find_element(By.ID, 'dropzone-file').send_keys(os.path.abspath(file_path))
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'identification-start'))
    ).click()

    # Wait for result elements to be displayed
    time.sleep(5)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'image-display'))
    )
    assert driver.find_element(By.ID, 'kondisi-beras').is_displayed(), "Rice condition not displayed."
    assert driver.find_element(By.ID, 'warna-beras').is_displayed(), "Rice color not displayed."
    assert driver.find_element(By.ID, 'kesimpulan-beras').is_displayed(), "Rice conclusion not displayed."
    assert driver.find_element(By.ID, 'accuracy-display').is_displayed(), "Accuracy display not shown."

@pytest.mark.usefixtures("browser")
def test_navigation(browser):
    # Test navigation across the pages
    time.sleep(5)
    browser.find_element(By.ID, 'about-bar').click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'index-button'))
    ).click()

    time.sleep(5)
    browser.find_element(By.ID, 'identify-bar').click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'index-button'))
    ).click()

    time.sleep(5)
    browser.find_element(By.ID, 'about-footer').click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'index-button'))
    ).click()

    time.sleep(5)
    browser.find_element(By.ID, 'feedback-footer').click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'index-button'))
    ).click()

    time.sleep(5)

@pytest.mark.usefixtures("browser")
def test_identify(browser):
    # Test the identification feature
    time.sleep(5)
    browser.find_element(By.ID, 'btn-identify').click()
    time.sleep(5)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'dropzone-file'))
    )

    # Test different images
    sample_files = [
        'C:/Users/adamg/Desktop/AI AND DATASET/Rice Model/Test Samples/Sample (1).jpg',
        'C:/Users/adamg/Desktop/AI AND DATASET/Rice Model/Test Samples/Gambar WhatsApp 2025-01-09 pukul 20.47.18_433dfa5d.jpg',
        'C:/Users/adamg/Desktop/AI AND DATASET/Rice Model/Test Samples/Gambar WhatsApp 2025-01-09 pukul 20.47.21_c3fffd89.jpg',
    ]

    for file_path in sample_files:
        upload_and_check_results(browser, file_path)
        browser.find_element(By.ID, 'identify-re').click()

    # Return to home page
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'index-button'))
    ).click()

