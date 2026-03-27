import allure
import requests
from requests import Response
from services.repository.models.create_repository_model import CreateRepositoryModel
from services.repository.models.get_repository_model import GetRepositoryModel
from config.headers import Headers


class RepositoryAPIService:
    def __init__(self):
        self._base_url = 'https://api.github.com'
        self._headers = Headers()

    @allure.step('Get a repository')
    def get_repository(self, owner: str, repo: str) -> GetRepositoryModel | Response:
        """
        Получение репозитория
        :param owner: Владелец репозитория
        :param repo: Название репозитория
        """
        response = requests.get(
            url=f'{self._base_url}/repos/{owner}/{repo}',
            headers=self._headers.get_headers()
        )
        if response.status_code == 200:
            assert response.status_code == 200, response.json()
            return GetRepositoryModel(**response.json())
        print('STATUS CODE:', response.status_code)
        return response

    @allure.step('Create a repository')
    def create_repository(self, body, authorized: bool = True) -> CreateRepositoryModel | Response:
        """
        Создание репозитория
        :param body: Тело запроса
        :param authorized: Авторизован ли юзер
        :return:
        """
        response = requests.post(
            url=f'{self._base_url}/user/repos',
            headers=self._headers.get_headers(authorized),
            json=body
        )
        if response.status_code == 201:
            assert response.status_code == 201, response.json()
            return CreateRepositoryModel(**response.json())
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
        return response