from selenium.webdriver.common.by import By


class RegistrationLocators:
    FIELD_LAST_NAME = (By.XPATH, "//p[text()='Фамилия']/../following::input[1]")
    FIELD_FIRST_NAME = (By.XPATH, "//p[text()='Имя']/../following::input[1]")

    FIELD_SURNAME = (By.XPATH, "//p[text()='Отчество']/../following::input[1]")
    CLICK_FIELD_DATE_OF_BIRTH = (By.XPATH, "//p[text()='Дата рождения']")
    FIELD_DATE_OF_BIRTH = (By.XPATH, "//p[text()='Дата рождения']/../following::input[1]")
    FIELD_EMAIL = (By.XPATH, "//p[text()='Электронная почта']/../following::input[1]")
    FIELD_LOGIN = (By.XPATH, "//p[text()='ВОШ-логин']/../following::input[1]")
    FIELD_TELEPHONE = (By.XPATH, "//p[text()='Телефон']/../following::input[1]")
    FIELD_SNILS = (By.XPATH, "//p[text()='СНИЛС']/../following::input[1]")
    FIELD_PROFESSION = (By.XPATH, "//p[text()='Профессия']/../following::input[1]")
    FIELD_COUNTRY = (By.XPATH, "//select[@class='ui-schema-auth-form__country-select ui-textinput__input-input-reset ']")
    FIELD_COUNTRY_RUSSIA = (By.XPATH, "//option[contains(text(), 'Россия') or contains(text(), 'Russia')]")
    FIELD_CITY = (By.XPATH, "//p[text()='Город']/../following::input[1]")
    FIELD_NAME_OF_ORGANIZATION = (By.XPATH, "//p[text()='Название организации']/../following::input[1]")
    FIELD_SCHOOL = (By.XPATH, "//p[text()='Школа']/../following::input[1]")
    FIELD_CLASS_SCHOOL = (By.XPATH, "//p[text()='Класс']/../following::input[1]")

    RADIO_BUTTON_MAIN_OLYMPICS = (By.XPATH, "//span[text()='Основная олимпиада']")
    RADIO_BUTTON_ADDITIONAL_OLYMPICS = (By.XPATH, "//span[text()='Дополнительная олимпиада']")

    CHECK_BOX_DATA = (By.XPATH, "//p[contains(text(), 'подтверждаю')]/ancestor::div[contains(@class, 'ui-schema-auth-form-deep')]//label[contains(@class, 'ui-checkbox')]/input")
    CHECK_BOX_CONSENT = (By.XPATH, "//p[contains(text(), 'Даю согласие')]/ancestor::div[contains(@class, 'ui-schema-auth-form-deep')]//label[contains(@class, 'ui-checkbox')]/input")
    CHECK_BOX_READ_RULES = (By.XPATH, "//p[contains(text(), 'прочитал')]/ancestor::div[contains(@class, 'ui-schema-auth-form-deep')]//label[contains(@class, 'ui-checkbox')]/input")
    BUTTON_GO_TO_TESTING = (By.XPATH, "//span[contains(@class, 'ui-button__content') and contains(text(), 'Перейти к тестированию')]")
    BUTTON_GO_TO_TESTING_DISABLED = (By.CSS_SELECTOR, ".ui-button-disabled")

    INVALID_ERROR_EMAIL = (By.XPATH, "//*[text()='Неверный email']")
    INVALID_ERROR_LOGIN = (By.XPATH, "//*[text()='Неверный ВОШ-логин. Попробуйте ещё раз']")
    INVALID_ERROR_SNILS = (By.XPATH, "//*[text()='СНИЛС должен содержать только цифры']")
    INVALID_ERROR_SNILS2 = (By.XPATH, "//*[text()='СНИЛС должен состоять ровно из 11 цифр']")




