from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    def calc(a,b):
        return str(a+b)
        
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    
    a_element = browser.find_element_by_id("num1")
    b_element = browser.find_element_by_id("num2")
    a = int(a_element.text)
    b = int(b_element.text)
    y = calc(a,b)
    
    result = Select(browser.find_element_by_tag_name("select"))
    result.select_by_value(y)
    
    button = browser.find_element_by_class_name("btn")
    button.click()
    

finally:
    time.sleep(10)
    browser.quit()