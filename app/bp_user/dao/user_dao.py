import json

from json import JSONDecodeError


class UserDAO:
    """Создаем класс обработчик всех действий с данными"""

    def __init__(self, path):
        """Инициализатор пути"""
        self.path = path

    def load_file(self):
        """загрузка (путь к файлу self.path) json файла и перевод его в список словарей
        (возвращает его под именем ---posts---)
        """
        try:
            with open(self.path, "r", encoding='utf-8') as file:
                posts = json.load(file)
                return posts
        except FileNotFoundError:
            return "По указанному пути файл не найден"
        except JSONDecodeError:
            return "Файл не удается преобразовать"

    def get_posts_by_user(self, user_name):
        """возвращает список (---posts_for_name---) словарей постов определенного пользователя"""
        if type(user_name) not in [str]:
            raise TypeError("Имя пользователя должно быть строкой")
        # Список для выдачи None(для получения ошибки ValueError) при отсутствии запрошенного имени
        names = []
        posts_for_name = []
        # получение списка из json
        posts = self.load_file()
        for post in posts:
            if user_name.lower() == post['poster_name'].lower():
                posts_for_name.append(post)
                names.append(post["poster_name"])
        # Вывод ошибки при отсутствии запрошенного имени пользователя(---poster_name---) в файле posts.json
        if user_name not in names:
            raise ValueError("Пользователь не найден")
        else:
            return posts_for_name
