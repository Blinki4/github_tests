import pytest
import allure

from dto.repository import Repository
from test_data import credentials


@pytest.mark.api
@allure.title('API создание репозитория')
def test_create_repo_api(create_repo_endpoint, delete_repo):
    repository = Repository(
        name=f'{credentials.new_repo_name}',
        description='description'
    )
    create_repo_endpoint.create_repo(repository, authorized=True)
    assert create_repo_endpoint.status_code == 201
    assert create_repo_endpoint.name == credentials.new_repo_name


@pytest.mark.api
@allure.title('API создание приватного репозитория')
def test_create_private_repo(create_repo_endpoint, delete_repo):
    repository = Repository(
        name=f'{credentials.new_repo_name}',
        description='description',
        private=True
    )
    create_repo_endpoint.create_repo(repository, authorized=True)
    assert create_repo_endpoint.status_code == 201
    assert create_repo_endpoint.is_private


@pytest.mark.api
@allure.title('API создание репозитория с существующим именем')
def test_create_repo_with_existing_name(create_repo_endpoint, delete_repo):
    repository = Repository(
        name=f'{credentials.new_repo_name}',
        description='description'
    )
    create_repo_endpoint.create_repo(repository, authorized=True)
    assert create_repo_endpoint.status_code == 201
    create_repo_endpoint.create_repo(repository, authorized=True)
    assert create_repo_endpoint.status_code == 422


@pytest.mark.api
@allure.title('API создание репозитория без авторизации')
def test_create_repo_unauthorized(create_repo_endpoint):
    repository = Repository(
        name=f'{credentials.new_repo_name}',
        description='description'
    )
    create_repo_endpoint.create_repo(repository, authorized=False)
    assert create_repo_endpoint.status_code == 401
    assert create_repo_endpoint.message == 'Requires authentication'



@pytest.mark.api
@allure.title('API получение существующего репозитория')
def test_get_existing_repo():
    ...