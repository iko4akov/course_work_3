import json

from json import JSONDecodeError


class PostDAO:
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
        # Вывод ошибки при отсутствии запрошенного номера поста(---pk---) в файле posts.json
        if 0 > pk or pk > len(posts):
            raise ValueError(f"Не верный номер поста укажите: от 0 до {len(posts)} включительно")
        for post in posts:
            if post["pk"] == pk:
                post_fined = post
        return post_fined

    def get_comments_by_post_id(self, post_id):
        """возвращает список словарей(---comments_for_post---) с комментариями определенного поста"""
        # Обработчик ошибки если не правильный формат id поста
        if type(post_id) not in [int]:
            raise TypeError("Не верный формат id поста")

        comments_for_post = []
        comments = self.load_file()

        # Вывод ошибки при отсутствии запрошенного номера поста(---post_id---) в файле comments.json
        if post_id > len(comments) or post_id < 0:
            raise ValueError(f"Не верный номер поста укажите: от 0 до {len(comments)} включительно")

        # Создание списка с коментами к искомому посту(---post_id---)
        for comment in comments:
            if comment["post_id"] == post_id:
                comments_for_post.append(comment)
        return comments_for_post
