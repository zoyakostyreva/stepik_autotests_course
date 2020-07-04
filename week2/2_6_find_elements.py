from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("https://totaldict.ru/shop/30509/")
    # добавляем товар в корзину
    add_button = browser.find_element_by_css_selector(".buy-button")
    add_button.click()

    # открываем страницу второго товара
    browser.get("https://totaldict.ru/shop/30510/")

    # добавляем товар в корзину
    add_button = browser.find_element_by_css_selector(".buy-button")
    add_button.click()

   # тестовый сценарий
   # открываем корзину
   browser.get("https://totaldict.ru/personal/cart/")

   # ищем все добавленные товары
   goods = browser.find_elements_by_css_selector(".description")

    # проверяем, что количество товаров равно 2
    assert len(goods) == 2