from selenium import webdriver
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)


    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("+")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("+")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("+")
    input4 = browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
# закрываем браузер после всех манипуляций
    browser.quit()
