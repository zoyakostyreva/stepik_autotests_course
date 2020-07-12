import random

def test_is_new_user_registered_successfully(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    browser.implicitly_wait(5)

    button1 = browser.find_element_by_id("login_link")
    button1.click()

    input1 = browser.find_element_by_id("id_registration-email")
    a = str(random.random())
    input1.send_keys("user" + a + "@gmail.com")

    input2 = browser.find_element_by_id("id_registration-password1")
    input2.send_keys("12Password!")
    input3 = browser.find_element_by_id("id_registration-password2")
    input3.send_keys("12Password!")

    button2 = browser.find_element_by_name("registration_submit")
    button2.click()

    message = browser.find_element_by_css_selector("#messages div.alertinner")
    assert "Thanks for registering!" in message.text
