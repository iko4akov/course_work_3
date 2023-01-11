import json

from json import JSONDecodeError


class MainDAO:
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


    def get_count_comment(self, comments):
        """Получает данные коментов, загруззает посты,
        возвращает все коменты к определенному посту в виде списка словарей"""
        com_post = {}
        posts = self.load_file()
        for i in range(len(posts)):
            count = 0
            for comment in comments:
                if comment["post_id"] == i + 1:
                    count += 1
            com_post[i + 1] = count
        return com_post
