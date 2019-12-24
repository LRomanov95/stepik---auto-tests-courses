from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    picture = browser.find_element_by_id("treasure")
    element = picture.get_attribute('valuex')
    print(element)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(element)
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







