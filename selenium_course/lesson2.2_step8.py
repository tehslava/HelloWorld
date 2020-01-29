from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_class_name("form-group>.form-control")
    name.send_keys("John")
    surname = browser.find_element_by_class_name("form-group>.form-control:nth-child(4)")
    surname.send_keys("Doe")
    mail = browser.find_element_by_class_name("form-group>.form-control:nth-child(6)")
    mail.send_keys("john.doe@yahoo.com")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'meh.txt')
    upload = browser.find_element_by_id("file")
    upload.send_keys(file_path)
    
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()