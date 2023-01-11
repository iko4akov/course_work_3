from app.bp_main.dao.main_dao import MainDAO
import pytest
from config.development import POSTS_PATH, COMMENT_PATH


# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре

@pytest.fixture()
def posts_dao():
    posts_dao_instance = MainDAO(POSTS_PATH)
    comment_dao_instance = MainDAO(COMMENT_PATH)
    return posts_dao_instance, comment_dao_instance


# Задаем, какие ключи ожидаем получать в постах
keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


class TestPostsDAO:

    def test_load_file(self, posts_dao):
        """ Проверяем, верный ли список posts возвращается """
        posts_load, comment_load = posts_dao
        posts = posts_load.load_file()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"


    def test_get_by_pk(self, posts_dao):
        """ Проверяем, возвращается словарь, длина списка словаря больше 0,
         что ключ больше нуля, """
        posts_load, comment_load = posts_dao
        posts = posts_load.load_file()
        comments = comment_load.load_file()
        com_post = posts_load.get_count_comment(comments)
        assert type(com_post) == dict, "возвращается не словарь"
        assert len(com_post) > 0, "возвращается словарь без ключей"
        assert min(com_post.keys()) > 0, "неверное значение ключа"
        assert len(posts) == len(com_post), "что то не то с длиной"
