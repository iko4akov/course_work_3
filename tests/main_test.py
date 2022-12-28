import pytest
from main.utils import PostHandler

POSTS_PATH = "../data/posts.json"


class TestHandler:
    def test_init_(self, path):
        pass

    def test_load_posts(self):
        pass

    def test_load_comments(self):
        pass

    def test_get_posts_by_user(self):
        with pytest.raises(TypeError):
            test = PostHandler(POSTS_PATH)
            test.get_posts_by_user(1235)

    def test_get_comments_by_post_id(self):
        pass

    def test_search_posts(self):
        pass

    def test_get_post_by_pk(self):
        pass
