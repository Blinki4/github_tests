import allure
import requests
from requests import Response
from config.headers import Headers
from services.users.models.get_user_response_model import GetUserResponseModel


class UsersAPIService:
    def __init__(self):
        self._base_url = 'https://api.github.com/users'
        self._headers = Headers()

    @allure.step('Get a user')
    def get_user(self, username: str) -> GetUserResponseModel | Response:
        """
        Получение пользователя
        :param username: Имя пользователя
        """
        response = requests.get(
            url=f'{self._base_url}/{username}',
            headers=self._headers.get_headers()
        )
        if response.status_code == 200:
            assert response.status_code == 200, response.json()
            return GetUserResponseModel(**response.json())
        return response