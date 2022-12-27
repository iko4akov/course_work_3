from flask import Blueprint, render_template, request

from main.utils import PostHandler

import logging

#Создаем блюпринт главной страницы
main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')
#Создаем блюпринт страницы поиска
search_blueprint = Blueprint("search_blueprint", __name__, template_folder='templates')
#Создаем блюпринт страницы с постами одного пользователя
user_blueprint = Blueprint("user_blueprint", __name__, template_folder='templates')
#Создаем блюпринт страницы с постом по айди
post_blueprint = Blueprint("post_blueprint", __name__, template_folder='templates')

# logging.basicConfig(filename="basic.log", level=logging.INFO)

@main_blueprint.route("/")
def index_page():
    post_handler = PostHandler('data/posts.json')
    posts = post_handler.load_posts()
    comment_handler = PostHandler('data/comments.json')
    comments = comment_handler.load_comments()
    com_post = post_handler.get_count_comment(posts, comments)
    return render_template("index.html", posts=posts, comments=comments, com_post=com_post)


@search_blueprint.route('/search')
def search_page():
    substr = request.args.get("s")
    post_handler = PostHandler('data/posts.json')
    fined_posts = post_handler.search_posts(substr)
    return render_template("search.html", fined_posts=fined_posts)


@user_blueprint.route('/user/<user_name>')
def user_page(user_name):
    post_handler = PostHandler('data/posts.json')
    posts_for_name = post_handler.get_posts_by_user(user_name)
    return render_template("user-feed.html", posts_for_name=posts_for_name, user_name=user_name)

@post_blueprint.route('/post/<int:id>')
def post_page(id):
    comment_handler = PostHandler('data/comments.json')
    post_handler = PostHandler('data/posts.json')
    post = post_handler.get_post_by_pk(id)
    comments = comment_handler.get_comments_by_post_id(id)
    return render_template("post.html", post=post, comments=comments)





