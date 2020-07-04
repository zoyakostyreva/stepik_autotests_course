from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Формула для расчета x
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("#treasure")
    x = x_element.get_attribute("valuex")
    # valuex = "662"
    y = calc(x)

    # Код всталяет результат выражения в поле "Ответ"

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Код нажимает на чек-бокс и на радиобатон

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что форма отправилась
    # ждем загрузки страницы
#    time.sleep(1)

finally:
    # Копируем код
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


