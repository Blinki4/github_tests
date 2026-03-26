import allure
import requests
from services.repository.models.get_repository_model import GetRepositoryModel
from config.headers import Headers


class RepositoryAPIService:
    def __init__(self):
        self._base_url = 'https://api.github.com'
        self._headers = Headers()

    @allure.step('Get a repository')
    def get_repository(self, owner: str, repo: str) -> GetRepositoryModel:
        """
        Получение репозитория
        :param owner: Владелец репозитория
        :param repo: Название репозитория
        """
        response = requests.get(
            url=f'{self._base_url}/{owner}/{repo}',
            headers=self._headers.get_headers(authorized=True)
        )
        assert response.status_code == 200, response.json()
        return GetRepositoryModel(**response.json())