import os

import dotenv
from flask import Flask, send_from_directory

from app.bp_api.view import api_blueprint
from app.bp_main.view import main_blueprint
from app.bp_post.view import post_blueprint
from app.bp_search.view import search_blueprint
from app.bp_user.view import user_blueprint

# Создание экземпляр класса Flask
app = Flask(__name__)

dotenv.load_dotenv(override=True)

# В зависимости от значения CONFIG подключаем тот или другой конфиг
if os.environ.get("CONFIG") == "debelopment":
    app.config.from_pyfile("config/development.py")
    POSTS_PATH = app.config.get('POSTS_PATH')
    COMMENT_PATH = app.config.get('COMMENT_PATH')
else:
    app.config.from_pyfile("config/production.py")
    POSTS_PATH = app.config.get('POSTS_PATH')
    COMMENT_PATH = app.config.get('COMMENT_PATH')

# Регистрация блюпринта главной страницы
app.register_blueprint(main_blueprint)
# Регистрация блюпринта одного поста
app.register_blueprint(post_blueprint)
# Регистрация блюпринта поисковой страницы с результатами поиска
app.register_blueprint(search_blueprint)
# Регистрация блюпринта страницы пользователя
app.register_blueprint(user_blueprint)
#Регистрация блюпринтов API
app.register_blueprint(api_blueprint, url_prefix="/GET/api/posts")


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
    """Позволяет использовать директорию с файлами upload (оставил тут, чтоб не потерять)"""
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
