from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.mark.test1
def test_is_button_add_to_basket_present_on_page_coder_at_work(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(5)

    # Ищем на странице кнопку добавления товара в корзину
    try:
        button = WebDriverWait(browser, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".btn-add-to-basket")))
        found = True

    # Если кнопку не нашли (возникла ошибка), то выполняем этот кусок кода
    except:
        found = False

    assert found == True, "Button is not found"

@pytest.mark.test2
def test_is_button_add_to_basket_present_on_page_hacking_exposed_wireless(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    browser.get(link)

    time.sleep(5)

    # Ищем на странице кнопку добавления товара в корзину
    try:
        button = WebDriverWait(browser, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".btn-add-to-basket")))
        found = True

    # Если кнопку не нашли (возникла ошибка), то выполняем этот кусок кода
    except:
        found = False

    assert found == True, "Button is not found"

if __name__ == '__main__':
    test_is_button_add_to_basket_present_on_page_coder_at_work()

    test_is_button_add_to_basket_present_on_page_hacking_exposed_wireless()

