import json

from json import JSONDecodeError


class ApiDAO:
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


    def get_post_by_pk(self, pk):
        """Возвращает словарь с данными для одного поста по его идентификатору"""
        post_fined = {}
        posts = self.load_file()
        # Вывод ошибки при отсутствии запрошенного номера поста(---pk---) в файле posts.json
        if 0 > pk or pk > len(posts):
            raise ValueError(f"Не верный номер поста укажите: от 0 до {len(posts)} включительно")
        for post in posts:
            if post["pk"] == pk:
                post_fined = post
        return post_fined

    def save_posts_to_json(self, posts):
        """Сохраняет новый список словарей в json файл"""
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(posts, file)

    def add_post(self, post):
        """Добавляет новый пост(словарь) в список словарей"""
        posts = self.load_file()
        posts.append(post)
        self.save_posts_to_json(posts)
