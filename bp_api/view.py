from flask import Blueprint, jsonify

import logging

from bp_api.dao.api_dao import ApiDAO


POSTS_PATH = 'data/posts.json'


# Создаем или получаем новый логгер
logger = logging.getLogger("basic")
# Создаем ему обработчик(бывает консольный и файловый) в котором указываю имя файла сохранения логов
# и кодировку для винды
file_handler = logging.FileHandler("api.log", encoding="utf-8")
# Создаем новое форматирование (объект класса Formatter)
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
# Применяем форматирование к обработчику
file_handler.setFormatter(formatter_one)
# Добавляем обработчик к журналу
logger.addHandler(file_handler)
# Задаем уровень логера
logger.setLevel(logging.INFO)


# Создаем блюпринт API всех постов
api_blueprint = Blueprint("api_posts_blueprint", __name__, template_folder='templates', url_prefix="/GET/api/posts")


@api_blueprint.get("/")
def get_api_page():
    """Возвращает полный список постов в виде JSON-списка"""
    posts = ApiDAO(POSTS_PATH)
    data = posts.load_file()
    logger.info("Запрос /api/posts")
    return jsonify(data)


@api_blueprint.get("/<int:post_id>")
def get_api_one_page(post_id):
    """Возвращает список поста в виде JSON-списка"""
    posts = ApiDAO(POSTS_PATH)
    data = posts.get_post_by_pk(post_id)
    logger.info(f"Запрос /api/posts/{post_id}")
    return jsonify(data)
