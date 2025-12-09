import allure

from locators import registration_locators
from locators.confirmation_email_locators import confirmationEmailLocators
from pages.base_method import BaseMethod
from locators.registration_locators import RegistrationLocators

class RegistrationPage(BaseMethod):

    @allure.step("Заполнение формы регистрации")
    def fill_registration_form(self, last_name,
                                            first_name,
                                            surname,
                                            date_of_birth,
                                            email,
                                            login,
                                            telephone,
                                            SNILS,
                                            profession,
                                            country,
                                            city,
                                            name_of_organization,
                                            school,
                                            class_school):

        self.send_keys_to_input(RegistrationLocators.FIELD_LAST_NAME, last_name)
        self.send_keys_to_input(RegistrationLocators.FIELD_FIRST_NAME, first_name)
        self.send_keys_to_input(RegistrationLocators.FIELD_SURNAME, surname)
        self.click_element(RegistrationLocators.CLICK_FIELD_DATE_OF_BIRTH)
        self.send_keys_to_input(RegistrationLocators.FIELD_DATE_OF_BIRTH, date_of_birth)
        self.send_keys_to_input(RegistrationLocators.FIELD_EMAIL, email)
        self.send_keys_to_input(RegistrationLocators.FIELD_LOGIN, login)
        self.send_keys_to_input(RegistrationLocators.FIELD_TELEPHONE, telephone)
        self.send_keys_to_input(RegistrationLocators.FIELD_SNILS, SNILS)
        self.send_keys_to_input(RegistrationLocators.FIELD_PROFESSION, profession)
        self.click_element(RegistrationLocators.FIELD_COUNTRY)
        self.click_element(RegistrationLocators.FIELD_COUNTRY_RUSSIA)
        self.send_keys_to_input(RegistrationLocators.FIELD_CITY, city)
        self.send_keys_to_input(RegistrationLocators.FIELD_NAME_OF_ORGANIZATION, name_of_organization)
        self.send_keys_to_input(RegistrationLocators.FIELD_SCHOOL, school)
        self.send_keys_to_input(RegistrationLocators.FIELD_CLASS_SCHOOL, class_school)

        self.click_element(RegistrationLocators.CHECK_BOX_DATA)
        self.click_element(RegistrationLocators.CHECK_BOX_CONSENT)
        self.click_element(RegistrationLocators.CHECK_BOX_READ_RULES)

    @allure.step("Клик по кнопке 'Перейти к тестированию'")
    def click_button_go_to_testing(self, timeout=10):
        self.click_element(RegistrationLocators.BUTTON_GO_TO_TESTING)

    @allure.step("клик на 'Дополнительная олимпиада'")
    def click_additional_olympics(self):
        self.click_element(RegistrationLocators.RADIO_BUTTON_ADDITIONAL_OLYMPICS)

    @allure.step("клик на 'Основная олимпиада'")
    def click_main_olympics(self):
        self.click_element(RegistrationLocators.RADIO_BUTTON_MAIN_OLYMPICS)

    @allure.step("Выбрать тип олимпиады")
    def select_olympics_type(self, radio_button):
        """
        Выбрать тип олимпиады по номеру радиокнопки
        :param radio_button: 0 - основная олимпиада, 1 - дополнительная олимпиада
        """
        if radio_button == 0:
            self.click_main_olympics()
        else:
            self.click_additional_olympics()

    @allure.step("Получить текст выбранной олимпиады")
    def get_olympics_text(self, radio_button):
        """
        Получить текст выбранной олимпиады
        :param radio_button: 0 - основная олимпиада, 1 - дополнительная олимпиада
        :return: текст элемента
        """
        if radio_button == 0:
            return self.get_text_by_locator(confirmationEmailLocators.MAIN_OLYMPICS)
        else:
            return self.get_text_by_locator(confirmationEmailLocators.ADDITIONAL_OLYMPICS)

    @allure.step("Заполнение формы регистрации не валидными данными")
    def invalid_registration_form(self, last_name,
                                   first_name,
                                   surname,
                                   date_of_birth,
                                   email,
                                   login,
                                   telephone,
                                   SNILS,
                                   profession,
                                   country,
                                   city,
                                   name_of_organization,
                                   school,
                                   class_school):

        self.send_keys_to_input(RegistrationLocators.FIELD_LAST_NAME, last_name)
        self.send_keys_to_input(RegistrationLocators.FIELD_FIRST_NAME, first_name)
        self.send_keys_to_input(RegistrationLocators.FIELD_SURNAME, surname)
        self.click_element(RegistrationLocators.CLICK_FIELD_DATE_OF_BIRTH)
        self.send_keys_to_input(RegistrationLocators.FIELD_DATE_OF_BIRTH, date_of_birth)
        self.send_keys_to_input(RegistrationLocators.FIELD_EMAIL, email)
        self.send_keys_to_input(RegistrationLocators.FIELD_LOGIN, login)
        self.send_keys_to_input(RegistrationLocators.FIELD_TELEPHONE, telephone)
        self.send_keys_to_input(RegistrationLocators.FIELD_SNILS, SNILS)
        self.send_keys_to_input(RegistrationLocators.FIELD_PROFESSION, profession)
        self.click_element(RegistrationLocators.FIELD_COUNTRY)
        self.click_element(RegistrationLocators.FIELD_COUNTRY_RUSSIA)
        self.send_keys_to_input(RegistrationLocators.FIELD_CITY, city)
        self.send_keys_to_input(RegistrationLocators.FIELD_NAME_OF_ORGANIZATION, name_of_organization)
        self.send_keys_to_input(RegistrationLocators.FIELD_SCHOOL, school)
        self.send_keys_to_input(RegistrationLocators.FIELD_CLASS_SCHOOL, class_school)

        self.click_element(RegistrationLocators.CHECK_BOX_DATA)
        self.click_element(RegistrationLocators.CHECK_BOX_CONSENT)
        self.click_element(RegistrationLocators.CHECK_BOX_READ_RULES)

    @allure.step("Проверяем, что кнопка неактивна по атрибуту disabled")
    def is_button_disabled(self):
        button = self.wait_for_element(RegistrationLocators.BUTTON_GO_TO_TESTING_DISABLED)
        disabled_attribute = button.get_attribute("disabled")

        # Возвращает True, если кнопка отключена (disabled)
        # get_attribute вернет 'true' если disabled есть, None если нет
        return disabled_attribute is not None and disabled_attribute != "false"

    @allure.step("получаем ошибку email")
    def get_error_email(self):
        return self.get_text_by_locator(RegistrationLocators.INVALID_ERROR_EMAIL)

    @allure.step("ввод только email")
    def input_email(self, email):
        self.send_keys_to_input(RegistrationLocators.FIELD_EMAIL, email)


    @allure.step("получаем ошибку логина")
    def get_error_login(self):
        return self.get_text_by_locator(RegistrationLocators.INVALID_ERROR_LOGIN)

    @allure.step("ввод только login")
    def input_login(self, login):
        self.send_keys_to_input(RegistrationLocators.FIELD_LOGIN, login)


    @allure.step("Проверяет обе возможные ошибки СНИЛС")
    def get_error_SNILS(self):
        try:
        # Сначала проверяем первую ошибку
            element = self.driver.find_element(*RegistrationLocators.INVALID_ERROR_SNILS)
            if element.is_displayed() and element.text:
                return element.text
        except:
            pass

        try:
        # Затем проверяем вторую ошибку
            element = self.driver.find_element(*RegistrationLocators.INVALID_ERROR_SNILS2)
            if element.is_displayed() and element.text:
                return element.text
        except:
            pass
        return None  # Если ошибка не найдена


    @allure.step("ввод только СНИЛС")
    def input_SNILS(self, SNILS):
        self.send_keys_to_input(RegistrationLocators.FIELD_SNILS, SNILS)

