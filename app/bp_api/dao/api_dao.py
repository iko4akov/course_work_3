import json

from json import JSONDecodeError


class ApiDAO:
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


    def get_post_by_pk(self, pk):
        """Принимает число(идентификатор) Возвращает словарь с данными для одного поста по его идентификатору"""
        post_fined = {}
        posts = self.load_file()
        # Вывод ошибки при отсутствии запрошенного номера поста(pk) в файле posts.json
        if 0 > pk or pk > len(posts):
            raise ValueError(f"Не верный номер поста укажите: от 0 до {len(posts)} включительно")
        for post in posts:
            if post["pk"] == pk:
                post_fined = post
        return post_fined

    def save_posts_to_json(self, posts):
        """Принимает новые данные и перезаписывает файл"""
        try:
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(posts, file, ensure_ascii=False)
        except FileNotFoundError:
            return "По указанному пути файл не найден"
        except JSONDecodeError:
            return "Файл не удается преобразовать"

    def add_post(self, post):
        """Добавляет новый пост(словарь) в список словарей, после этой функции необходимо перезаписать"""
        posts = self.load_file()
        posts.append(post)
        self.save_posts_to_json(posts)
