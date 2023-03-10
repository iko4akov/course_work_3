
class TestMain:

    def test_root_status_all(self, test_client):
        """ Проверяем, получается ли нужный статус-код и """
        response = test_client.get('/GET/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус-код всех постов неверный"

    def test_root_content_all(self, test_client):
        response = test_client.get('/GET/api/posts', follow_redirects=True)
        assert type(response.data.decode("utf-8")) == str , "Возвращается не строка"


    def test_root_status_one(self, test_client):
        """ Проверяем, получается ли нужный статус-код и """
        response = test_client.get('/GET/api/posts/<int:post_id>', follow_redirects=True)
        assert response.status_code == 200, "Статус-код всех постов неверный"

    def test_root_content_one(self, test_client):
        response = test_client.get('/GET/api/posts', follow_redirects=True)
        assert type(response.data.decode("utf-8")) == str, "Возвращается не строка"