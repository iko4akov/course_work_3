from flask import Flask, send_from_directory, jsonify
from bp_main.view import main_blueprint, search_blueprint, user_blueprint, post_blueprint, POSTS_PATH
from bp_main.dao.main_dao import PostsDAO
import logging


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


# Создание экземпляр класса Flask
app = Flask(__name__)

# Регистрация блюпринтов для работы приложения
app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(post_blueprint)


@app.errorhandler(404)
def not_found(e):
    """Вьюшка обработки ошибки 400"""
    return f"<h1>Нет такой страницы<h1>\n<h2>Код ошибки:<h2>\n{e}"


@app.errorhandler(500)
def not_found(e):
    """Вьюшка обработки ошибки 500"""
    return f"<h1>Ошибка на сервере<h1>\n<h2>Код ошибки:<h2>\n {e}"


@app.route("/uploads/<path:path>")
def static_dir(path):
    """Позволяет использовать директорию с файлами upload"""
    return send_from_directory("uploads", path)


@app.get("/GET/api/posts")
def get_api_page():
    """Возвращает полный список постов в виде JSON-списка"""
    posts = PostsDAO(POSTS_PATH)
    data = posts.load_file()
    logger.info("Запрос /api/posts")
    print(data)
    return jsonify(data)


@app.get("/GET/api/posts/<int:post_id>")
def get_api_one_page(post_id):
    """Возвращает полный список постов в виде JSON-списка"""
    posts = PostsDAO(POSTS_PATH)
    data = posts.get_post_by_pk(post_id)
    logger.info(f"Запрос /api/posts/{post_id}")
    return jsonify(data)


if __name__ == "__main__":
    app.run()
