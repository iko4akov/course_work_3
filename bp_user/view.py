from flask import Blueprint, render_template

from bp_user.dao.user_dao import UserDAO

POSTS_PATH = 'data/posts.json'

# Создаем блюпринт страницы с постами одного пользователя
user_blueprint = Blueprint("user_blueprint", __name__, template_folder='templates')


@user_blueprint.get('/user/<user_name>')
def user_page(user_name):
    post_handler = UserDAO(POSTS_PATH)
    posts_for_name = post_handler.get_posts_by_user(user_name)
    return render_template("user-feed.html", posts_for_name=posts_for_name, user_name=user_name)
