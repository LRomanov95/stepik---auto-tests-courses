from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html" 
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Леонид")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Романов")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("leonid.romanov@chulakov.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'Romanov.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    element.click
    time.sleep(2)
    button = browser.find_element_by_class_name("btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
