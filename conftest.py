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
