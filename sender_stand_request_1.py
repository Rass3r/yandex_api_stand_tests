# Импорт необходимых модулей и данных для запроса
import requests
import configuration
import data

# Определение функции для отправки POST-запроса на поиск наборов по продуктам
def post_products_kits(products_ids):
    # Отправка POST-запроса с использованием URL из конфигурации, данных о продуктах и заголовков
    # Возвращается объект ответа, полученный от сервера
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids)  # Тело запроса содержит ID продуктов в формате JSON

# Вызов функции с передачей списка ID продуктов из файла data.py
response = post_products_kits(data.products_ids)

# Вывод HTTP-статус кода ответа и тела ответа в формате JSON
# Это позволяет проверить успешность выполнения запроса и посмотреть результаты поиска наборов
print(response.status_code)
print(response.json()) 
