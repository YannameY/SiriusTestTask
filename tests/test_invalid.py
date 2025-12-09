import time

import allure
import pytest

import data
from data import invalid_Credentials
from pages.registration_method import RegistrationPage


class Test_negative:
    @allure.title("Негативный тест кнопки 'Перейти к тестированию'")
    @allure.feature("Валидация формы")
    @allure.story("Кнопка неактивна при невалидных данных")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    @pytest.mark.registration
    @pytest.mark.ui
    def test_invalid(self, driver):
        registration_method = RegistrationPage(driver)
        with allure.step("1. Заполнение формы невалидными данными"):
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
        with allure.step("2. Проверка, что кнопка неактивна"):
            assert registration_method.is_button_disabled(), \
                "Кнопка должна быть неактивной при невалидных данных"


    @allure.title("Негативный тест поля электронной почты")
    @allure.feature("Валидация формы")
    @allure.story("Проверка сообщения об ошибке для email")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.negative
    @pytest.mark.email
    @pytest.mark.field_validation
    def test_invalid_email(self, driver):
        registration_method = RegistrationPage(driver)
        with allure.step("1. Ввод невалидного email"):
            registration_method.input_email(invalid_Credentials.email)
        with allure.step("2. Получение текста ошибки"):
            actual_text = registration_method.get_error_email()
        with allure.step("3. Проверка соответствия текста ошибки"):
            expected_text = data.error_message_filed.message_error_email

        assert actual_text == expected_text, \
        f"Ожидалось: {expected_text}, получено: {actual_text}"


    @allure.title("Негативный тест поля логин")
    @allure.feature("Валидация формы")
    @allure.story("Проверка сообщения об ошибке для ВОШ-логина")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.negative
    @pytest.mark.login
    @pytest.mark.field_validation
    def test_invalid_login(self, driver):
        registration_method = RegistrationPage(driver)
        with allure.step("1. Ввод невалидного логина"):
            registration_method.input_login(invalid_Credentials.login)
        with allure.step("2. Получение текста ошибки"):
            actual_text = registration_method.get_error_login()
        with allure.step("3. Проверка соответствия текста ошибки"):
            expected_text = data.error_message_filed.message_error_login

        assert actual_text == expected_text, \
            f"Ожидалось: {expected_text}, получено: {actual_text}"


    @allure.title("Негативный тест поля СНИЛС")
    @allure.feature("Валидация формы")
    @allure.story("Проверка сообщения об ошибке для СНИЛС")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.negative
    @pytest.mark.snils
    @pytest.mark.field_validation
    @pytest.mark.parametrize("snils_value, expected_error_index",
        [
            (invalid_Credentials.SNILS, 0),  # индекс 0: "СНИЛС должен состоять ровно из 11 цифр"
            (invalid_Credentials.SNILS2, 1)  # индекс 1: "СНИЛС должен содержать только цифры"
        ]
    )
    def test_invalid_SNILS(self, driver, snils_value, expected_error_index):
        registration_method = RegistrationPage(driver)
        with allure.step(f"1. Ввод невалидного СНИЛС: {snils_value}"):
            registration_method.input_SNILS(snils_value)
        with allure.step("2. Получение текста ошибки"):
            actual_text = registration_method.get_error_SNILS()
        with allure.step("3. Получение ожидаемого текста ошибки"):
            expected_text = data.error_message_filed.message_error_SNILS[expected_error_index][1]
        with allure.step("4. Проверка соответствия текста ошибки"):
            assert actual_text == expected_text, \
            f"Ожидалось: {expected_text}, получено: {actual_text}"