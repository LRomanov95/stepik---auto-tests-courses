from selenium import webdriver
import math
import time
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)
    chekbox = browser.find_element_by_id("robotCheckbox")
    chekbox.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    time.sleep(2)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally: 
    time.sleep(30)
    browser.quit()
    






