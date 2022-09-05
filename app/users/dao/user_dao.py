import json
from app.users.dao.user import User


class UserDAO:

    def __int__(self, path):
        self.path = path

    def load_data(self):
        """ Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def write_data_in_base(self):
        """Записываем данные из даты в таблицу user sql"""
        users = self.load_data()
        list_users = []
        for user in users:
            user["id"] = User(firs_name=user["first_name"],
                              last_name=user["last_name"],
                              age=user["age"],
                              email=user["email"],
                              role=user["role"],
                              phone=user["phone"]
                              )
            list_users.append(user["id"])



