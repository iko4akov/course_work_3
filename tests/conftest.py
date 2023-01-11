import pytest
import run


@pytest.fixture()
# создаем фикстуру для тестирования всех вьюшек (api, main, post, search, user)
def test_client():
    app = run.app
    return app.test_client()
