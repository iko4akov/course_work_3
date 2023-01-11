from flask import Flask, send_from_directory
from bp_main.view import main_blueprint
from bp_post.view import post_blueprint
from bp_search.view import search_blueprint
from bp_user.view import user_blueprint
from bp_api.view import api_blueprint


# Создание экземпляр класса Flask
app = Flask(__name__)

# Регистрация блюпринта главной страницы
app.register_blueprint(main_blueprint)

# Регистрация блюпринта одного поста
app.register_blueprint(post_blueprint)

# Регистрация блюпринта поисковой страницы с результатами поиска
app.register_blueprint(search_blueprint)

# Регистрация блюпринта страницы пользователя
app.register_blueprint(user_blueprint)

#Регистрация блюпринтов API
app.register_blueprint(api_blueprint)


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


if __name__ == "__main__":
    app.run()
