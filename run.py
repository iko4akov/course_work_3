from flask import Flask, send_from_directory
from main.view import main_blueprint, search_blueprint, user_blueprint, post_blueprint

POSTS_PATH = "/data/posts.json"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(post_blueprint)


@app.errorhandler(404)
def not_found(e):
    """Вьюшка обоработки ошибки 400"""
    return f"<h1>Нет такой страницы<h1>\n<h2>Код ошибки:<h2>\n{e}"


@app.errorhandler(500)
def not_found(e):
    """Вьшка обработки ошибки 500"""
    return f"<h1>Ошибка на сервере<h1>,\n<h2>Код ошибки:<h2>\n {e}"


@app.route("/uploads/<path:path>")
def static_dir(path):
    """Позволяет использовать директорию с файлами upload"""
    return send_from_directory("uploads", path)

if __name__ == "__main__":
    app.run()
