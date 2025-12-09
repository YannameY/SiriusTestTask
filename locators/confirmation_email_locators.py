from selenium.webdriver.common.by import By


class confirmationEmailLocators:
    MAIN_OLYMPICS = (By.XPATH, "//*[text()='Автостесты. Основная олимпиада']")
    ADDITIONAL_OLYMPICS = (By.XPATH, "//*[text()='Автостесты. Дополнительная олимпиада']")

    @staticmethod
    def radio_button(v):
        return By.XPATH, f'//*[text()="{v}"]'
