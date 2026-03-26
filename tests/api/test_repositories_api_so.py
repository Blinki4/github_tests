import os

from dotenv import load_dotenv

load_dotenv()

class TestRepositoriesApi:

    def test_get_existing_repo_os(self, create_repo_with_api, repository_api_service):
        repository_api_service.get_repository(os.getenv('LOGIN'), os.getenv('PASSWORD'))
