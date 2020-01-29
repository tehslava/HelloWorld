from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    book = browser.find_element_by_id("book")
    book.click()

    ok_element = browser.find_element_by_id("input_value")
    ok = ok_element.text
    final_ok = calc(ok)
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(final_ok)
    
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()