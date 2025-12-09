from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import pytest

from curl import main_site


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=options)
    driver.get(main_site)
    yield driver
    driver.quit()

def pytest_configure(config):
    """Конфигурация pytest"""
    config.addinivalue_line(
        "markers",
        "email: тесты для проверки email"
    )
    config.addinivalue_line(
        "markers",
        "login: тесты для проверки логина"
    )
    config.addinivalue_line(
        "markers",
        "snils: тесты для проверки СНИЛС"
    )
    config.addinivalue_line(
        "markers",
        "negative: негативные тесты"
    )
    config.addinivalue_line(
        "markers",
        "registration: тесты регистрации"
    )