import json

from json import JSONDecodeError


class UserDAO:
    """Создаем класс обработчик всех действий с данными"""

    def __init__(self, path):
        """Инициализатор пути к необходимым файлам, в данном случая к файлу с постами, и к файлу с коментами"""
        self.path = path

    def load_file(self):
        """Открывает файл, загрузка (путь к файлу self.path) json файла и перевод его в список словарей
        для дальнейшей работы питона
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
        """Получает имя пользователя
        возвращает список с постами по имени пользователя"""
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
