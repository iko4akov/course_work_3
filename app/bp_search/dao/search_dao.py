import json

from json import JSONDecodeError


class SearchDAO:
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


    def search_posts(self, substr):
        """получает строку, по ней ищет совпадения в контенте каждого поста
        возвращает в шаблон найденые посты"""
        searh_list = []
        load_posts = self.load_file()
        for post in load_posts:
            if substr.lower() in post['content'].lower():
                searh_list.append(post)
        return searh_list
