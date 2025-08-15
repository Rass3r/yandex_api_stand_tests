# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

def get_user_body(first_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.user_body.copy()
    # изменение значения в поле firstName
    current_body["firstName"] = first_name
    # возвращается новый словарь с нужным значением firstName
    return current_body

    # Функция для негативной проверки 
    # В ответе ошибка: "Не все необходимые параметры были переданы"
def negative_assert_no_first_name(user_body):
        # В переменную response сохрани результат вызова функции
        response = sender_stand_request.post_new_user(user_body)
    
        # Проверь, что код ответа — 400
        assert response.status_code == 400
    
        # Проверь, что в теле ответа атрибут "code" — 400
        assert response.json()["code"] == 400
    
        # Проверь текст в теле ответа в атрибуте "message"
        assert response.json()["message"] == "Не все необходимые параметры были переданы"

# Тест 10. Ошибка 
# В запросе нет параметра firstName
def test_create_user_no_first_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную user_body
    # Иначе можно потерять данные из исходного словаря
    user_body = data.user_body.copy()
    # Удаление параметра firstName из запроса
    user_body.pop("firstName")
    # Проверка полученного ответа
    negative_assert_no_first_name(user_body)

# Тест 11. Ошибка 
# Параметр fisrtName состоит из пустой строки
def test_create_user_empty_first_name_get_error_response():
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body("")
    # Проверка полученного ответа
    negative_assert_no_first_name(user_body) 

# Тест 12. Ошибка 
# Тип параметра firstName: число
def test_create_user_number_type_first_name_get_error_response():
        # В переменную user_body сохраняется обновлённое тело запроса
        user_body = get_user_body(12)
        # В переменную user_response сохраняется результат запроса на создание пользователя:
        response = sender_stand_request.post_new_user(user_body)
    
        # Проверка кода ответа
        assert response.status_code == 400
    