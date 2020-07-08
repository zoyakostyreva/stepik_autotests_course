from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

# @pytest.mark.parametrize('language', ["ru", "es", "fr"])
# def test_language_should_change(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
#     browser.get(link)

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser
    print("\nquit browser..")
    browser.quit()





