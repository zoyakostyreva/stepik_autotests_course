# Тест-кейс № 4. Регистрация нового пользователя. Корректная регистрация.

# Ожидаемый результат: сайт успешно зарегистрировал нового пользователя.
# Появилось сообщение "Спасибо за регистрацию!"

from selenium import webdriver
import time
import random
import pytest

@pytest.fixture(scope="session")
def browser(request):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    yield browser
    print("\nquit browser..")
    browser.quit()

def main():
    test_is_new_user_registered()

def test_is_new_user_registered(browser):
    browser.implicitly_wait(5)

    # 1) Найти кнопку "Войти или зарегистрироваться".
    button1 = browser.find_element_by_id("login_link")
    button1.click()

    # 2) На форме "Зарегистрироваться" в поле "Адрес электронной почты" ввести email.
    input1 = browser.find_element_by_id("id_registration-email")
    a = str(random.random())
    input1.send_keys("user" + a + "@gmail.com")

    # 3) В поля "Пароль" и "Повторите пароль" ввести "12Password!".
    input2 = browser.find_element_by_id("id_registration-password1")
    input2.send_keys("12Password!")
    input3 = browser.find_element_by_id("id_registration-password2")
    input3.send_keys("12Password!")

    # 4) Нажать на кнопку "Зарегистрироваться".
    button2 = browser.find_element_by_name("registration_submit")
    button2.click()

    message = browser.find_element_by_css_selector("#messages div.alertinner")
    assert "Спасибо за регистрацию!" in message.text


if __name__ == '__main__':
    main()


