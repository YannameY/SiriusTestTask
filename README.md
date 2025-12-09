## Тестовое задание Сириус курсы

<hr>

## <h>Project: Автостесты. Основная олимпиада</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла              | Содержание файла                                  |
|-----------------------------|---------------------------------------------------|
| confirmation_email_locators | Локаторы страницы подтверждения email             |
| registration_locators.py    | Локаторы страницы формы регистрации олимпиады     |
| base_method.py              | Базовые методы для работы поиска, ожидания, ввода |
| registration_method.py      | Методы для страницы регистрации                   |
| test_invalid.py             | Негативные тесты                                  |
| test_successful.py          | Положительные тесты                               |
| conftest.py                 | Фикстура для настройки браузера                   |
| curl.py                     | URL главной страницы регистрации                  |
| data.py                     | Статичные данные для работы с тестами             |
| requirements.txt            | Файл с зависимостями                              |
| allure_results.dir          | Папка с отчетами Allure                           |

