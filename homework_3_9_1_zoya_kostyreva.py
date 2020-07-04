from selenium import webdriver
import time
import random

# Первый тест-кейс. Проверяем, что в поле email важно записать с символом @.
def emailcheck():
    # 1) Найти кнопку "Войти или зарегистрироваться".
    button1 = browser.find_element_by_id("login_link")
    button1.click()

    # 2) Найти форму "Зарегистрироваться".
    # 3) В поле "Адрес электронной почты" ввести "kostyreva".
    input1 = browser.find_element_by_id("id_registration-email")
    input1.send_keys("kostyreva")

    # 4) В поля "Пароль" и "Повторите пароль" ввести "12Password!".
    input2 = browser.find_element_by_id("id_registration-password1")
    input2.send_keys("12Password!")
    input3 = browser.find_element_by_id("id_registration-password2")
    input3.send_keys("12Password!")

    # 5) Нажать на кнопку "Зарегистрироваться".
    button2 = browser.find_element_by_name("registration_submit")
    button2.click()

    # Ожидаемый результат: сайт не дает возможность зарегистрироваться, выдает сообщение
    # "Адрес электронной почты должен содержать символ "@".
    # "В адресе "kostyreva" отсутствует символ "@".
    # Печатаем сообщение об ошибке.
    message = browser.find_element_by_id("id_registration-email")
    assert "отсутствует символ \"@\"" in message.get_attribute("validationMessage")

# Второй тест-кейс. Проверяем длину пароля.
def passwordlength():
    # 1) Найти кнопку "Войти или зарегистрироваться".
    button1 = browser.find_element_by_id("login_link")
    button1.click()

    # 2) Найти форму "Зарегистрироваться".
    # 3) В поле "Адрес электронной почты" ввести "user1@gmail.com".
    input1 = browser.find_element_by_id("id_registration-email")
    input1.send_keys("user1@gmail.com")

    # 4) В поля "Пароль" и "Повторите пароль" ввести "12".
    input2 = browser.find_element_by_id("id_registration-password1")
    input2.send_keys("12")
    input3 = browser.find_element_by_id("id_registration-password2")
    input3.send_keys("12")

    # 5) Нажать на кнопку "Зарегистрироваться".
    button2 = browser.find_element_by_name("registration_submit")
    button2.click()

    message = browser.find_element_by_css_selector("#id_registration-password2 + span.error-block")
    assert "короткий" in message.text

# Третий тест-кейс. Проверяем, что оба пароля совпадают.
def equalpassword():
    # 1) Найти кнопку "Войти или зарегистрироваться".
    button1 = browser.find_element_by_id("login_link")
    button1.click()

    # 2) Найти форму "Зарегистрироваться".
    # 3) В поле "Адрес электронной почты" ввести "user1@gmail.com".
    input1 = browser.find_element_by_id("id_registration-email")
    input1.send_keys("user1@gmail.com")

    # 4) В поле "Пароль" ввести "12Password!".
    # 5) В поле "Повторите пароль" ввести "Password!".
    input2 = browser.find_element_by_id("id_registration-password1")
    input2.send_keys("12Password!")
    input3 = browser.find_element_by_id("id_registration-password2")
    input3.send_keys("Password!")

    # 6) Нажать на кнопку "Зарегистрироваться".
    button2 = browser.find_element_by_name("registration_submit")
    button2.click()

    message = browser.find_element_by_css_selector("#id_registration-password2 + span.error-block")
    assert "не совпадают" in message.text

# Четвертый тест-кейс. Регистрация пользователя, который уже существует.
def useralreadyexists():
    # 1) Найти кнопку "Войти или зарегистрироваться".
    button1 = browser.find_element_by_id("login_link")
    button1.click()

    # 2) Найти форму "Зарегистрироваться".
    # 3) В поле "Адрес электронной почты" ввести "user2@gmail.com".
    input1 = browser.find_element_by_id("id_registration-email")
    input1.send_keys("user2@gmail.com")

    # 4) В поля "Пароль" и "Повторите пароль" ввести "12Password!".
    input2 = browser.find_element_by_id("id_registration-password1")
    input2.send_keys("12Password!")
    input3 = browser.find_element_by_id("id_registration-password2")
    input3.send_keys("12Password!")

    # 5) Нажать на кнопку "Зарегистрироваться".
    button2 = browser.find_element_by_name("registration_submit")
    button2.click()

    message = browser.find_element_by_css_selector("#id_registration-email + span.error-block")
    assert "уже зарегистрирован" in message.text

# Пятый тест-кейс. Корректная регистрация пользователя.
def registrationcorrect():
    # 1) Найти кнопку "Войти или зарегистрироваться".
    button1 = browser.find_element_by_id("login_link")
    button1.click()

    # 2) Найти форму "Зарегистрироваться".
    # 3) В поле "Адрес электронной почты" ввести email.
    input1 = browser.find_element_by_id("id_registration-email")
    a = str(random.random())
    input1.send_keys("user"+a+"@gmail.com")

    # 4) В поля "Пароль" и "Повторите пароль" ввести "12Password!".
    input2 = browser.find_element_by_id("id_registration-password1")
    input2.send_keys("12Password!")
    input3 = browser.find_element_by_id("id_registration-password2")
    input3.send_keys("12Password!")

    # 5) Нажать на кнопку "Зарегистрироваться".
    button2 = browser.find_element_by_name("registration_submit")
    button2.click()

    message = browser.find_element_by_css_selector("#messages div.alertinner")
    assert "Спасибо за регистрацию!" in message.text

# Шестой тест-кейс. Добавляем товар в корзину.
def additemtocart():
    # 1) Найти секцию "Просмотр магазина" с выпадающим меню.
    # 2) Перейти в раздел "Books".
    browser.find_element_by_css_selector("#browse .dropdown-submenu > [tabindex='-1'] ").click()

    # 3-4) Найти первый на странице товар и добавить его в корзину.
    element = browser.find_element_by_css_selector("[title='Coders at Work']").parent
    button = element.c

    button1 = browser.find_element_by_css_selector(".btn-primary")
    button1.click()

    # Результат: Товар добавлен в корзину, появляется сообщение, что книга добавлена в корзину.
    message = browser.find_element_by_css_selector("#messages .alertinner:first-of-type")
    assert "добавлен в вашу корзину" in message.text




try:
    browser = webdriver.Chrome()
    # Открыть в браузере страницу: http://selenium1py.pythonanywhere.com/ru/.
    browser.get("http://selenium1py.pythonanywhere.com/ru/")
    browser.implicitly_wait(5)

    # Запускаем первый тест-кейс
    emailcheck()

    # Запускаем второй тест-кейс
    passwordlength()

    # Запускаем третий тест-кейс
    equalpassword()

    # Запускаем четвертый тест-кейс
    useralreadyexists()

    # Запускаем пятый тест-кейс
    registrationcorrect()

    # Запускаем шестой тест-кейс
    additemtocart()

finally:
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
