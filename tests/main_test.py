import pytest
import run

class TestMain:

    def test_root_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код и """
        response = test_client.get('/meow', follow_redirects=True)
        assert response.status_code == 200, f"Статус-код {response.status_code} всех постов неверный"

    # def test_api(self, keys_fixture):
        # response = run.test_client().get('/')
        #
        # assert response.status_code == 200
        # assert type(response.json) == dict
        # assert set(response.json.keys()) == keys_fixture


    def test_init_(self, path):
        pass

    def test_load_posts(self):
        pass

    def test_load_comments(self):
        pass

    def test_get_posts_by_user(self):
        pass

    def test_get_comments_by_post_id(self):
        pass

    def test_search_posts(self):
        pass

    def test_get_post_by_pk(self):
        pass
