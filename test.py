from selenium import webdriver
import time
import os

os.system('python app.py')
time.sleep(17)
# Open the browser
driver = webdriver.Chrome()
# Open the website
driver.get('http://127.0.0.1:5000')
time.sleep(7)
# Press on the identify button
driver.find_element_by_id('btn-identify').click()
time.sleep(7)
# Upload the image into the form
driver.find_element_by_id('submit-images').send_keys(os.path.abspath('C:/Users/adamg/Downloads/rice-2380808_960_720.jpg'))
time.sleep(5)
# Start the identification
driver.find_element_by_id('identification-start').click()
time.sleep(10)
# Check if the correct text is displayed
assert driver.find_element_by_id('kondisi-beras').text == 'Kondisi Beras: Full ( Broken (<=15%) )'
assert driver.find_element_by_id('warna-beras').text == 'Warna Beras: Putih'
assert driver.find_element_by_id('kesimpulan-beras').text == 'Ini adalah Beras Premium. Dapat diketahui dengan jumlah butir patah yang lebih sedikit ( Broken (<=15%) ) sehingga dapat dipastikan ini adalah beras premium.'
time.sleep(5)
# DONE
driver.quit()



# def test_app():
#     # run the app.py
#     os.system('python app.py')
#     # Open the browser
#     driver_path = 'D:/chromedriver_win32/chromedriver.exe'
#     driver = webdriver.Chrome(executable_path=driver_path)
#     # Open the website
#     driver.get('http://127.0.0.1:5000')
#     time.sleep(7)
#     # Press on the identify button
#     driver.find_element_by_id('btn-identify').click()
#     time.sleep(7)
#     # Upload the image into the form
#     driver.find_element_by_id('submit-images').send_keys(os.path.abspath('C:/Users/adamg/Downloads/rice-2380808_960_720.jpg'))
#     time.sleep(5)
#     # Start the identification
#     driver.find_element_by_id('identification-start').click()
#     time.sleep(10)
#     # Check if the correct text is displayed
#     assert driver.find_element_by_id('kondisi-beras').text == 'Kondisi Beras: Full ( Broken (<=15%) )'
#     assert driver.find_element_by_id('warna-beras').text == 'Warna Beras: Putih'
#     assert driver.find_element_by_id('kesimpulan-beras').text == 'Ini adalah Beras Premium. Dapat diketahui dengan jumlah butir patah yang lebih sedikit ( Broken (<=15%) ) sehingga dapat dipastikan ini adalah beras premium.'
#     time.sleep(5)
#     driver.quit()


