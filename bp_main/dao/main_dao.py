import json

from json import JSONDecodeError


def get_count_comment(posts, comments):
    """Получение списка cловарей в формате ид поста: кол-во коментариев"""
    com_post = {}
    for i in range(len(posts)):
        count = 0
        for comment in comments:
            if comment["post_id"] == i + 1:
                count += 1
        com_post[i + 1] = count
    return com_post


class PostsDAO:
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

    def search_posts(self, substr):
        """возвращает список(---searh_list---) словарей с постами по ключевому слову"""
        searh_list = []
        load_posts = self.load_file()
        for post in load_posts:
            if substr.lower() in post['content'].lower():
                searh_list.append(post)
        return searh_list

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
