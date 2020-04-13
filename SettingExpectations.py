from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_id('book')
    button.click()
    x_element = browser.find_element_by_id('input_value')
    textarea_answer = browser.find_element_by_id("answer")
    textarea_answer.send_keys(calc(x_element.text))
    button1=browser.find_element_by_id('solve')
    button1.click()
finally:
    time.sleep(15)
    browser.quit()