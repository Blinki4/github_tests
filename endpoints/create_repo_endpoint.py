import requests


from requests import Response

from dto.repository import Repository
from endpoints.base_endpoint import BaseEndpoint
from dataclasses import asdict



class CreateRepoEndpoint(BaseEndpoint):
    url: str = '/user/repos'
    status_code: int
    name: str
    description: str
    is_private: bool
    message: str


    def create_repo(self, body: Repository, authorized: bool = True) -> Response:
        response = requests.post(
            f'{self.base_url}{self.url}',
            headers = {
                'Accept': 'application/vnd.github+json',
                'Authorization': f'Bearer {self.token}' if authorized else None,
                'X-GitHub-Api-Version': '2022-11-28'
            },
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