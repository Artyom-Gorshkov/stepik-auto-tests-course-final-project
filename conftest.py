import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language of browser")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language in ("ru", "en", "es", "fr"):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru, en, es, or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()
