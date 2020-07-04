from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button1 = browser.find_element_by_css_selector("button.trollface")
    button1.click()

    # Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
    # который возвращает массив имён всех вкладок.
    # Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    # Переключаемся в новое окно в браузере
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button2 = browser.find_element_by_tag_name("button")
    button2.click()

finally:
    # Копируем код
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
