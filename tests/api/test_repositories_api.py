import os
import allure
import pytest
from dotenv import load_dotenv

load_dotenv()

@allure.epic('Репозитории API')
class TestRepositoriesAPI:

    @pytest.mark.api
    @allure.title('API создание репозитория')
    def test_create_repository_api(self, repositories_api_service, delete_repository_req):
        response = repositories_api_service.create_repository()
        assert response.name == os.getenv('REPO_NAME')

    @pytest.mark.api
    @allure.title('API создание приватного репозитория')
    def test_create_private_repository_api(self, repositories_api_service, delete_repository_req):
        response = repositories_api_service.create_repository(private=True)
        assert response.private

    @pytest.mark.api
    @allure.title('API создание репозитория с существующим именем')
    def test_create_repository_with_existing_name(
            self,
            create_repository_req,
            repositories_api_service,
            delete_repository_req
        ):
        response = repositories_api_service.create_repository()
        assert response.status_code == 422

    @pytest.mark.api
    @allure.title('API создание репозитория без авторизации')
    def test_create_repository_unauthorized(self, repositories_api_service):
        response = repositories_api_service.create_repository(authorized=False)
        assert response.status_code == 401
        assert response.json()['message'] == 'Requires authentication'

    @pytest.mark.api
    @allure.title('API получение существующего репозитория')
    def test_get_existing_repository_api(self, create_repository_req, repositories_api_service, delete_repository_req):
        repositories_api_service.get_repository(
            owner=os.getenv('LOGIN'),
            repo=os.getenv('REPO_NAME')
        )

    @pytest.mark.api
    @allure.title('API получение несуществующего репозитория')
    def test_get_non_existing_repository(self, repositories_api_service):
        response = repositories_api_service.get_repository(
            owner=os.getenv('LOGIN'),
            repo='bulbozhabchik'
        )
        assert response.status_code == 404

    @pytest.mark.api
    @allure.title('API получение репозитория у несуществующего пользователя')
    def test_get_non_existing_repository(self, repositories_api_service):
        response = repositories_api_service.get_repository(
            owner='bulbozhabchik',
            repo='bulbozhabchik'
        )
        assert response.status_code == 404

    @pytest.mark.api
    @allure.title('API удаление репозитория')
    def test_delete_repository(self, create_repository_req, repositories_api_service, delete_repository_req):
        response = repositories_api_service.delete_repository(
            owner=os.getenv('LOGIN'),
            repo=os.getenv('REPO_NAME')
        )
        assert response.status_code == 204

    @pytest.mark.api
    @allure.title('Удаление несуществующего репозитория')
    def test_delete_non_existing_repository(self, repositories_api_service):
        response = repositories_api_service.delete_repository(
            owner=os.getenv('LOGIN'),
            repo=os.getenv('REPO_NAME')
        )
        assert response.status_code == 404