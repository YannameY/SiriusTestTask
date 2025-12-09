class Credentials:
    last_name = "Смирнов"
    first_name = "Андрей"
    surname = "Дмитриевич"
    date_of_birth = "19.09.2010"
    email = "yavyazovikov@gmail.com"
    login = "v00.000.000"
    telephone = "89997775533"
    SNILS = "00000000000"
    profession = "IT"
    country = ""
    city = "Санкт-Петербург"
    name_of_organization = "Тбанк"
    school = "13"
    class_school = "11"

class data:
    expected_answers = [
        [0, 'Автостесты. Основная олимпиада'],
        [1, 'Автостесты. Дополнительная олимпиада']
    ]

class invalid_Credentials:
    last_name = "Смирнов"
    first_name = "Андрей"
    surname = "Дмитриевич"
    date_of_birth = "19.09.2027"
    email = "yavyazovikovgmail.com"
    login = "v00.000.00q"
    telephone = "8999777553q"
    SNILS = "0000"
    SNILS2 = "0000000000q"
    profession = "IT"
    country = ""
    city = "Санкт-Петербург"
    name_of_organization = "Тбанк"
    school = "13"
    class_school = "11"

class error_message_filed:
    message_error_email = "Неверный email"
    message_error_login = "Неверный ВОШ-логин. Попробуйте ещё раз"

    message_error_SNILS = [
        [0, "СНИЛС должен состоять ровно из 11 цифр"],
        [1, "СНИЛС должен содержать только цифры"]
    ]

