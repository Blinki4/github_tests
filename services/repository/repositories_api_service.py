import allure
import requests
from requests import Response
from services.repository.models.create_repository_response_model import CreateRepositoryResponseModel
from services.repository.models.get_repository_response_model import GetRepositoryResponseModel
from config.headers import Headers
from services.repository.payloads import Payloads
from utils.helper import Helper


class RepositoriesAPIService(Helper):
    def __init__(self):
        self._base_url = 'https://api.github.com'
        self._headers = Headers()
        self._payloads = Payloads()

    @allure.step('Get a repository')
    def get_repository(self, owner: str, repo: str) -> GetRepositoryResponseModel | Response:
        """
        Получение репозитория
        :param owner: Владелец репозитория
        :param repo: Название репозитория
        """
        response = requests.get(
            url=f'{self._base_url}/repos/{owner}/{repo}',
            headers=self._headers.get_headers()
        )
        self.attach_response(response.json())
        if response.status_code == 200:
            assert response.status_code == 200, response.json()
            return GetRepositoryResponseModel(**response.json())
        return response

    @allure.step('Create a repository')
    def create_repository(self, private: bool = False, authorized: bool = True) -> CreateRepositoryResponseModel | Response:
        """
        Создание репозитория
        :param private: Приватность репозитория
        :param authorized: Авторизован ли юзер
        :return:
        """
        response = requests.post(
            url=f'{self._base_url}/user/repos',
            headers=self._headers.get_headers(authorized),
            json=self._payloads.create_repository(private)
        )
        self.attach_response(response.json())
        if response.status_code == 201:
            assert response.status_code == 201, response.json()
            return CreateRepositoryResponseModel(**response.json())
        return response

    @allure.step('Delete a repository')
    def delete_repository(self, owner: str, repo: str) -> Response:
        """
        Удаление репозитория
        :param owner: Владелец репозитория
        :param repo: Название репозитория
        :return:
        """
        response = requests.delete(
            url=f'{self._base_url}/repos/{owner}/{repo}',
            headers=self._headers.get_headers(),
        )
        # self.attach_response(response.json())
        return response