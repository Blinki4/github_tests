import requests
from config.headers import Headers
from services.search.models.search_user_response_model import SearchUserResponseModel

class SearchAPIService:
    def __init__(self):
        self._base_url = 'https://api.github.com/search'
        self._headers = Headers()

    def search_user(self, query: str) -> SearchUserResponseModel:
        response = requests.get(
            url=f'{self._base_url}/users?q={query}',
            headers=self._headers.get_headers()
        )
        assert response.status_code == 200, f'Status code: {response.status_code}'
        return SearchUserResponseModel(**response.json())