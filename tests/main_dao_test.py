from app.bp_main.dao.main_dao import MainDAO
import pytest

from config.development import POSTS_PATH


# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре

@pytest.fixture()
def posts_dao():
    posts_dao_instance = MainDAO(POSTS_PATH)
    return posts_dao_instance


# Задаем, какие ключи ожидаем получать в постах
keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
posts_dao_instance = posts_dao

class TestPostsDAO:

    def test_get_all(self, posts_dao_instance):
        """ Проверяем, верный ли список posts возвращается """
        posts = posts_dao_instance.load_file()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    # def test_get_by_pk(self, posts_dao_instance):
    #     """ Проверяем, верный ли post возвращается при запросе одного """
    #     post = posts_dao_instance.get_post_by_pk(1)
    #     assert type(post) == dict, "возвращается не словарь"
    #     assert post["pk"] == 1, "возвращается неправильный кандидат"
    #     assert set(post.keys()) == keys_should_be, "неверный список ключей"

