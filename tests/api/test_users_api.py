import pytest
import allure

from dto.get_user_response import GetUserResponse
from test_data import credentials


@pytest.mark.api
@allure.title('Получение пользователя')
@pytest.mark.parametrize('username', [f'{credentials.valid_login}', 'ivanushka-na-python'])
def test_get_user(get_user_endpoint, username):
    response = get_user_endpoint.get_user(username)
    GetUserResponse(**response.json()) # Валидация JSON-схемы ответа
    assert get_user_endpoint.status_code == 200
    assert get_user_endpoint.login == username




@pytest.mark.api
@allure.title('Получение несуществующего пользователя')
def test_get_non_existing_user(get_user_endpoint):
    get_user_endpoint.get_user('BulboZhabchik')
    assert get_user_endpoint.status_code == 404
