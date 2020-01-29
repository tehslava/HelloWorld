from selenium import webdriver
import time
import math

try: 
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    text = browser.find_element_by_tag_name("input")
    text.send_keys(y)
    
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    
    button = browser.find_element_by_class_name("btn")
    button.click()
    

finally:
    time.sleep(10)
    browser.quit()