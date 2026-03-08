import allure
import requests

from requests import Response
from dto.get_user_response import GetUserResponse
from endpoints.base_endpoint import BaseEndpoint


class GetUserEndpoint(BaseEndpoint):
    login: str


    @allure.step('Получение пользователя')
    def get_user(self, username: str) -> GetUserResponse | Response:
        """
        Получение пользователя
        :param username: Имя пользователя
        """
        response = requests.get(
            f'{self.base_url}/users/{username}',
            headers=self.get_headers()
        )
        self.status_code = response.status_code
        if response.status_code == 200:
            self.login = response.json()['login']
            return GetUserResponse(**response.json()) # Валидация json схемы ответа
        return response