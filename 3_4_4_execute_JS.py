from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # Код всталяет результат выражения в поле "Ответ"

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Код нажимает на чек-бокс и на радиобатон

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # button.click()
    option2 = browser.find_element_by_id("robotsRule")
    button = browser.find_element_by_tag_name("button")

    # Мы можем заставить браузер дополнительно проскролить нужный элемент, чтобы он точно стал видимым.
    # В метод execute_script мы передали текст js-скрипта и найденный элемент button,
    # к которому нужно будет проскролить страницу.
    # После выполнения кода элемент button должен оказаться в верхней части страницы.
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Эта команда проскроллит страницу на 100 пикселей вниз:
    # browser.execute_script("window.scrollBy(0, 100);")
    option2.click()
    button.click()
    assert True



finally:
    # Копируем код
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
