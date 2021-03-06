import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
    parser.addoption('--browser', action='store', default='Chrome',
                     help="Choose browser: Chrome or Firefox")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser")

    if browser_name == 'Chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'Firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.maximize_window()
    browser.implicitly_wait(5)

    yield browser
    print("\nquit browser..")
    browser.quit()





