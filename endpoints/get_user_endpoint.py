import requests
from requests import Response

from endpoints.base_endpoint import BaseEndpoint


class GetUserEndpoint(BaseEndpoint):
    login: str

    def get_user(self, username: str) -> Response:
        response = requests.get(
            f'{self.base_url}/users/{username}',
            headers=self.get_headers()
        )
        self.status_code = response.status_code
        if response.status_code == 200:
            self.login = response.json()['login']
        return response