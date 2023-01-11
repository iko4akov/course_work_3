from flask import Blueprint, render_template, request


from app.bp_search.dao.search_dao import SearchDAO


POSTS_PATH = 'data/posts.json'


# Создаем блюпринт страницы поиска
search_blueprint = Blueprint("search_blueprint", __name__, template_folder='templates')


@search_blueprint.get('/search')
def search_page():
    """получает поисковой запрос
    загружает файл с постами и в нем ищет посты с поисковым запросом
    возвразщает в шаблон найденные посты"""
    substr = request.args.get("s")
    # Условие для отображения пустой страницы поиска
    if substr is None:
        substr = "anti_error_search_page"
        post_handler = SearchDAO(POSTS_PATH)
        fined_posts = post_handler.search_posts(substr)
    else:
        post_handler = SearchDAO(POSTS_PATH)
        fined_posts = post_handler.search_posts(substr)
    return render_template("search.html", fined_posts=fined_posts)
