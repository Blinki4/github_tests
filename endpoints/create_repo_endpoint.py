import requests
import allure

from requests import Response
from dto.repository import Repository
from endpoints.base_endpoint import BaseEndpoint
from dataclasses import asdict



class CreateRepoEndpoint(BaseEndpoint):
    url: str = '/user/repos'
    name: str
    description: str
    is_private: bool
    message: str


    @allure.step('Создание репозитория')
    def create_repo(self, body: Repository, authorized: bool = True) -> Response:
        """
        Создание репозитория
        :param body: Параметры репозитория
        :param authorized: Авторизован ли запрос
        """
        response = requests.post(
            f'{self.base_url}{self.url}',
            headers = self.get_headers(authorized),
            json = asdict(body)
        )
        self.status_code = response.status_code
        if response.status_code == 201:
            self.name = response.json()['name']
            self.description = response.json()['description']
            self.is_private = response.json()['private']
        if response.status_code == 401:
            self.message = response.json()['message']
        return response