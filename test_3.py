# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data
# эта функция меняет значения в параметре firstName
def get_user_body(first_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.user_body.copy()
    # изменение значения в поле firstName
    current_body["firstName"] = first_name
    # возвращается новый словарь с нужным значением firstName
    return current_body

    # Функция для негативной проверки
def negative_assert_symbol(first_name):
        # В переменную user_body сохраняется обновлённое тело запроса
        user_body = get_user_body(first_name)
        # В переменную response сохраняется результат запроса
        response = sender_stand_request.post_new_user(user_body)
        # Проверка, что код ответа равен 400
        assert response.status_code == 400
        # Проверка, что в теле ответа атрибут "code" равен 400
        assert response.json()["code"] == 400
        # Проверка текста в теле ответа в атрибуте "message"
        assert response.json()["message"] == "Имя пользователя введено некорректно. " \
                                             "Имя может содержать только русские или латинские буквы, " \
                                             "длина должна быть не менее 2 и не более 15 символов"

    # Тест 3. Ошибка 
    # Параметр fisrtName состоит из 1 символа
def test_create_user_1_letter_in_first_name_get_error_response():
        negative_assert_symbol("A")

# Тест 4. Ошибка 
# Параметр fisrtName состоит из 16 символов
def test_create_user_16_letter_in_first_name_get_error_response():
        negative_assert_symbol("Аааааааааааааааa")

# Тест 5. Успешное создание пользователя 
# Параметр fisrtName состоит из английских букв
def test_create_user_english_letter_in_first_name_get_success_response():
        positive_assert("QWErty")

# Тест 6. Успешное создание пользователя 
# Параметр fisrtName состоит из русских букв
def test_create_user_russian_letter_in_first_name_get_success_response():
        positive_assert("Мария")

# Тест 7. Ошибка 
# Параметр fisrtName состоит из слов с пробелами
def test_create_user_has_space_in_first_name_get_error_response():
        negative_assert_symbol("Человек и КО")

# Тест 8. Ошибка
# Параметр fisrtName состоит из строки спецсимволов
def test_create_user_has_special_symbol_in_first_name_get_error_response():
        negative_assert_symbol("№%@")

# Тест 9. Ошибка
# Параметр fisrtName состоит из строки с цифрами
def test_create_user_has_number_in_first_name_get_error_response():
        negative_assert_symbol("123")
    
    