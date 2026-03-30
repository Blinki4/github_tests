import pytest
import allure
import os
from dotenv import load_dotenv


load_dotenv()

class TestSearchAPI:
    def test_search_user(self, search_api_service):
        response = search_api_service.search_user(os.getenv('LOGIN'))
        assert response.items[0].login == os.getenv('LOGIN')