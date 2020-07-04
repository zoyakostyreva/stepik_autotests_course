from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код находит радиобатон
    people_radio = browser.find_element_by_id("peopleRule")

    # Первый способ проверки
    people_checked = people_radio.get_attribute("checked")
    #print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is not selected by default"

    # Второй способ проверки
    assert people_checked == "true", "People radio is not selected by default"
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None



finally:
# Копируем код
    time.sleep(10)
# закрываем браузер после всех манипуляций
    browser.quit()


