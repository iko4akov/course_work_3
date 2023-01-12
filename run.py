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
# Если честно практического применения в этой курсовой не нашел
if os.environ.get("CONFIG") == "debelopment":
    app.config.from_pyfile("config/development.py")
    #Для примера можно вытащить POSTS_PATH, использовать нельзя зацикливается импорт файла на файл
    POSTS_PATH = app.config.get("POSTS_PATH")
else:
    app.config.from_pyfile("config/production.py")


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

@app.get("/development")
def development_page():
    return f"<p>С целью отблагодарить материально разработчика обращаться: <h3>{os.environ.get('MAIL_Development')}</h3></p>" \
           f"Донаты и поддержка проекта: <h1>{os.environ.get('number_card')} сбер))</h1>\n" \
           f"Telegramm <h2>{os.environ.get('number_phone')}</h2>"


if __name__ == "__main__":
    app.run()
