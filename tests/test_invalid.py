import time

import allure
import pytest

import data
from data import invalid_Credentials
from pages.registration_method import RegistrationPage


class Test_negative:
    @allure.title("Негативный тест кнопки 'Перейти к тестированию'")
    @pytest.mark.something
    def test_invalid(self, driver):
        registration_method = RegistrationPage(driver)

        registration_method.invalid_registration_form(invalid_Credentials.last_name,
                                                   invalid_Credentials.first_name,
                                                   invalid_Credentials.surname,
                                                   invalid_Credentials.date_of_birth,
                                                   invalid_Credentials.email,
                                                   invalid_Credentials.login,
                                                   invalid_Credentials.telephone,
                                                   invalid_Credentials.SNILS,
                                                   invalid_Credentials.profession,
                                                   invalid_Credentials.country,
                                                   invalid_Credentials.city,
                                                   invalid_Credentials.name_of_organization,
                                                   invalid_Credentials.school,
                                                   invalid_Credentials.class_school)

        assert registration_method.is_button_disabled(), "Кнопка должна быть неактивной"

    @allure.title("Негативный тест поля электронной почты")
    @pytest.mark.something
    def test_invalid_email(self, driver):
        registration_method = RegistrationPage(driver)
        registration_method.input_email(invalid_Credentials.email)
        # Шаг 3: Получаем текст ошибки
        actual_text = registration_method.get_error_email()
        # Шаг 4: Ожидаемый текст из файла с сообщениями
        expected_text = data.error_message_filed.message_error_email
        # Шаг 5: Проверяем соответствие
        assert actual_text == expected_text, \
        f"Ожидалось: {expected_text}, получено: {actual_text}"


    @allure.title("Негативный тест поля логин")
    @pytest.mark.something
    def test_invalid_login(self, driver):
        registration_method = RegistrationPage(driver)
        registration_method.input_login(invalid_Credentials.login)
        # Шаг 3: Получаем текст ошибки
        actual_text = registration_method.get_error_login()
        # Шаг 4: Ожидаемый текст из файла с сообщениями
        expected_text = data.error_message_filed.message_error_login
        # Шаг 5: Проверяем соответствие
        assert actual_text == expected_text, \
            f"Ожидалось: {expected_text}, получено: {actual_text}"


    @allure.title("Негативный тест поля СНИЛС")
    @pytest.mark.parametrize("snils_value, expected_error_index",
        [
            (invalid_Credentials.SNILS, 0),  # индекс 0: "СНИЛС должен состоять ровно из 11 цифр"
            (invalid_Credentials.SNILS2, 1)  # индекс 1: "СНИЛС должен содержать только цифры"
        ]
    )
    def test_invalid_SNILS(self, driver, snils_value, expected_error_index):
        registration_method = RegistrationPage(driver)
        registration_method.input_SNILS(snils_value)
        # Получаем текст ошибки
        actual_text = registration_method.get_error_SNILS()
        # Получаем ожидаемый текст по индексу
        expected_text = data.error_message_filed.message_error_SNILS[expected_error_index][1]
        # Проверяем соответствие
        assert actual_text == expected_text, \
            f"Ожидалось: {expected_text}, получено: {actual_text}"