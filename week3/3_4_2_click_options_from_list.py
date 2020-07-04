from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# если вы получаете ошибку в духе "argument of type 'int' is not iterable",
# перепроверьте тип переменной, которую вы передаете в функцию поиска.
# Нужно передать строку!

try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    z = int(x) + int(y)
    # print(z)

    z = str(z)

    browser.find_element_by_tag_name("select").click()
    #browser.find_element_by_css_selector("option:nth-child(2)").click()
    browser.find_element_by_css_selector(f"[value='{z}']").click()

    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value(z)  # ищем элемент с нужным значением

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # Копируем код
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

