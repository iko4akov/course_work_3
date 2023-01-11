import json

from json import JSONDecodeError


class MainDAO:
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


    def get_count_comment(self, comments):
        """Получение списка cловарей в формате ид поста: кол-во коментариев"""
        com_post = {}
        posts = self.load_file()
        for i in range(len(posts)):
            count = 0
            for comment in comments:
                if comment["post_id"] == i + 1:
                    count += 1
            com_post[i + 1] = count
        return com_post
