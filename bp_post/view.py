from flask import Blueprint, render_template

from bp_post.dao.post_dao import PostDAO


POSTS_PATH = 'data/posts.json'

COMMENT_PATH = 'data/comments.json'


# Создаем блюпринт страницы с постом по айди
post_blueprint = Blueprint("post_blueprint", __name__, template_folder='templates')


@post_blueprint.get('/post/<int:pk>')
def post_page(pk):
    comment_handler = PostDAO(COMMENT_PATH)
    post_handler = PostDAO(POSTS_PATH)
    post = post_handler.get_post_by_pk(pk)
    comments = comment_handler.get_comments_by_post_id(pk)
    return render_template("post.html", post=post, comments=comments)