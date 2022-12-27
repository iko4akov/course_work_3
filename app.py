from flask import Flask, send_from_directory
from main.view import main_blueprint, search_blueprint, user_blueprint, post_blueprint

POSTS_PATH = "/data/posts.json"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(post_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    """Позволяет использовать директорию с файлами upload"""
    return send_from_directory("uploads", path)


app.run()
