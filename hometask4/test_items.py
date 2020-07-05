from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    test_is_button_add_to_basket_present()

def test_is_button_add_to_basket_present(browser):

    time.sleep(30)

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
    main()