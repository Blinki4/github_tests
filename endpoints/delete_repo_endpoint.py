import requests
import allure

from requests import Response
from endpoints.base_endpoint import BaseEndpoint
from test_data import credentials

class DeleteRepoEndpoint(BaseEndpoint):
    def __init__(self):
        super().__init__()
        self.url = f'{self.base_url}/repos/{credentials.valid_login}'


    @allure.step('Удаление репозитория')
    def delete_repo(self, repo_name: str) -> Response:
        """
        Удаление репозитория
        :param repo_name: Название репозитория
        """
        response = requests.delete(
            f'{self.url}/{repo_name}',
            headers=self.get_headers()
        )
        self.status_code = response.status_code
        return response