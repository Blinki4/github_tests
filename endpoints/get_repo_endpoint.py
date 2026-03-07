import requests
from requests import Response

from endpoints.base_endpoint import BaseEndpoint


class GetRepoEndpoint(BaseEndpoint):
    name: str
    owner: str

    def __init__(self):
        super().__init__()
        self.url = f'{self.base_url}/repos'


    def get_repo(self, owner: str, repo: str) -> Response:
        response = requests.get(
            f'{self.url}/{owner}/{repo}',
            headers={
                'Accept': 'application/vnd.github+json',
                'Authorization': f'Bearer {self.token}',
                'X-GitHub-Api-Version': '2022-11-28'
            }
        )
        self.status_code = response.status_code
        if response.status_code == 200:
            self.name = response.json()['name']
            self.owner = response.json()['owner']['login']
        return response