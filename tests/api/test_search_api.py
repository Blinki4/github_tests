import pytest
import allure
import os
from dotenv import load_dotenv

load_dotenv()

@allure.epic('Search service tests')
class TestSearchAPI:

    @pytest.mark.api
    @allure.title('Search a user')
    def test_search_user_api(self, search_api_service):
        response = search_api_service.search_user(query=os.getenv('LOGIN'))
        assert response.items[0].login == os.getenv('LOGIN')

    @pytest.mark.api
    @allure.title('Search a repository')
    def test_search_repository_api(self, search_api_service):
        response = search_api_service.search_repository(query='linux')
        found = False
        for repo in response.items:
            if repo.name == 'linux':
                found = True
        assert found

    @pytest.mark.api
    @allure.title('Поиск по несуществующему запросу')
    def test_search_repository_non_existing_query_api(self, search_api_service):
        response = search_api_service.search_repository(query='lkasjdljadhskdfhgksdjgfsdfkghj')
        assert response.total_count == 0

    def test_search_repository_for_language(self, search_api_service):
        response = search_api_service.search_repository(query='language:python')
        assert response.total_count > 0