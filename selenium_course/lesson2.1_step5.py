from selenium import webdriver
import time
import math

try: 
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    text = browser.find_element_by_tag_name("input")
    text.send_keys(y)
    
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    
    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()
    
    button = browser.find_element_by_class_name("btn")
    button.click()
    

finally:
    time.sleep(10)
    browser.quit()