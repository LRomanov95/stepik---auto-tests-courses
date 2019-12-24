from selenium import webdriver
import math
import time
def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    chekbox = browser.find_element_by_id("robotCheckbox")
    chekbox.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
