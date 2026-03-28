import os

import pytest
import allure
from dotenv import load_dotenv

load_dotenv()

@allure.epic('Users API')
class TestUsersAPI:

    @pytest.mark.api
    @allure.title('Получение пользователя')
    @pytest.mark.parametrize('username', [
        os.getenv('LOGIN'),
        'ivanushka-na-python',
        'torvalds'
    ])
    def test_get_user(self, users_api_service, username):
        response = users_api_service.get_user(username)
        assert response.login == username

    @pytest.mark.api
    @allure.title('Получение несуществующего пользователя')
    def test_get_non_existing_user(self, users_api_service):
        response = users_api_service.get_user('BulboZhabchik')
        assert response.status_code == 404