import requests
import allure
from config.headers import Headers
from services.search.models.search_repository_response_model import SearchRepositoryResponseModel
from services.search.models.search_user_response_model import SearchUserResponseModel

class SearchAPIService:
    def __init__(self):
        self._base_url = 'https://api.github.com/search'
        self._headers = Headers()

    @allure.step('Search a user')
    def search_user(
            self,
            query: str,
            sort: str = None,
            order: str = None,
            per_page: str = None,
            page: str = None
            ) -> SearchUserResponseModel:
        """
        Поиск пользователей
        :param query:
        :param sort: followers, repositories, joined
        :param order: asc, desc
        :param per_page:
        :param page:
        """
        response = requests.get(
            url=f'{self._base_url}/users',
            headers=self._headers.get_headers(),
            params={
                'q': query,
                'sort': sort,
                'order': order,
                'per_page': per_page,
                'page': page
            }
        )
        assert response.status_code == 200, f'Status code: {response.status_code}'
        return SearchUserResponseModel(**response.json())

    @allure.step('Search a repository')
    def search_repository(
            self,
            query: str,
            sort: str = None,  #
            order: str = None,  #
            per_page: str = None,
            page: str = None
    ) -> SearchRepositoryResponseModel:
        """
        Поиск репозиториев
        :param query:
        :param sort: stars, forks, help-wanted-issues, updated
        :param order: asc, desc
        :param per_page:
        :param page:
        """
        response = requests.get(
            url=f'{self._base_url}/repositories',
            headers=self._headers.get_headers(),
            params={
                'q': query,
                'sort': sort,
                'order': order,
                'per_page': per_page,
                'page': page
            }
        )
        assert response.status_code == 200, f'Status code: {response.status_code}'
        return SearchRepositoryResponseModel(**response.json())