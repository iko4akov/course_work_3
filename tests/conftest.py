import pytest
import run

# создаем фикстуру для тестирования всех вьюшек
@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()
