from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    element1 = browser.find_element_by_id("num1")
    a = int(element1.text)
    element2 = browser.find_element_by_id("num2")
    b = int(element2.text)
    x = a + b
    browser.find_element_by_tag_name("select").click()
    css_selector = "[value='{0}']".format(x);
    browser.find_element_by_css_selector(css_selector).click()
    time.sleep(1)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
