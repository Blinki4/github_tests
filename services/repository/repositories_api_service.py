import allure
import requests
from requests import Response
from services.repository.models.create_repository_response_model import CreateRepositoryResponseModel
from services.repository.models.get_repository_response_model import GetRepositoryResponseModel
from config.headers import Headers


class RepositoriesAPIService:
    def __init__(self):
        self._base_url = 'https://api.github.com'
        self._headers = Headers()

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
        if response.status_code == 200:
            assert response.status_code == 200, response.json()
            return GetRepositoryResponseModel(**response.json())
        return response

    @allure.step('Create a repository')
    def create_repository(self, body, authorized: bool = True) -> CreateRepositoryResponseModel | Response:
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
        return response