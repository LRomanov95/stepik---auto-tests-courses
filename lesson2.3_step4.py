from selenium import webdriver
import math
import time
def calc (x):
    return str (math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_class_name("btn")
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    element1 = browser.find_element_by_id("input_value")
    x = element1.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button2 = browser.find_element_by_class_name("btn-primary")
    button2.click()
finally:
    time.sleep(10)
    browser.quit()

    