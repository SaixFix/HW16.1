import json


def load_users():
    """ Загружает данные из файла users.json и возвращает обычный list"""
    with open("./data/users.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_offers():
    """ Загружает данные из файла offers.json и возвращает обычный list"""
    with open("./data/offers.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_orders():
    """ Загружает данные из файла offers.json и возвращает обычный list"""
    with open("./data/orders.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# todo удалить эту хрень

# def add_all():
#     """Записываем данные из даты в таблицы"""
#     users = load_users()
#     list_users = []
#     for user in users:
#         user["id"] = User(firs_name=user["first_name"],
#                           last_name=user["last_name"],
#                           age=user["age"],
#                           email=user["email"],
#                           role=user["role"],
#                           phone=user["phone"]
#                           )
#         list_users.append(user["id"])
