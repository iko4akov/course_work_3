from flask import Blueprint, render_template

from app.bp_main.dao.main_dao import MainDAO


POSTS_PATH = 'data/posts.json'

COMMENT_PATH = 'data/comments.json'

# Создаем блюпринт главной страницы
main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')


@main_blueprint.get("/")
def index_page():
    """Принимает путь к файлам(посты, коменты) возврашает в шаблон все посты и количество коментов к посту"""
    post_handler = MainDAO(POSTS_PATH)
    posts = post_handler.load_file()
    comment_handler = MainDAO(COMMENT_PATH)
    comments = comment_handler.load_file()
    com_post = comment_handler.get_count_comment(comments)
    return render_template("index.html", posts=posts, com_post=com_post)
