import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.confirmation_email_locators import confirmationEmailLocators


class BaseMethod:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимость элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.deiver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст по элементу")
    def get_text_by_locator(self, locator):
        element = self.wait_for_element(locator)
        return element.text
