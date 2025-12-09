
import allure
import pytest
from data import Credentials, data
from pages.registration_method import RegistrationPage


class TestTes:
    @allure.title("Тест успешной регистрации")
    @allure.feature("Регистрация")
    @allure.story("Успешное заполнение формы регистрации")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    @pytest.mark.registration
    @pytest.mark.smoke
    @pytest.mark.parametrize('radio_button, expected_text', data.expected_answers)
    def test_tes(self, driver, radio_button, expected_text):
        registration_method = RegistrationPage(driver)
        with allure.step("1. Заполнение формы регистрации валидными данными"):
            registration_method.fill_registration_form(Credentials.last_name,
                                                   Credentials.first_name,
                                                   Credentials.surname,
                                                   Credentials.date_of_birth,
                                                   Credentials.email,
                                                   Credentials.login,
                                                   Credentials.telephone,
                                                   Credentials.SNILS,
                                                   Credentials.profession,
                                                   Credentials.country,
                                                   Credentials.city,
                                                   Credentials.name_of_organization,
                                                   Credentials.school,
                                                   Credentials.class_school)
        with allure.step("2. Выбор типа олимпиады"):
            registration_method.select_olympics_type(radio_button)
        with allure.step("3. Нажатие кнопки 'Перейти к тестированию'"):
            registration_method.click_button_go_to_testing()
        with allure.step("4. Проверка текста выбранной олимпиады"):
            actual_text = registration_method.get_olympics_text(radio_button)
        assert actual_text == expected_text, f"Ожидалось: {expected_text}, получено: {actual_text}"



