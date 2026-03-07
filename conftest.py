import pytest
import requests

from dto.repository import Repository
from endpoints.create_repo_endpoint import CreateRepoEndpoint
from endpoints.get_repo_endpoint import GetRepoEndpoint
from pages.main_page import MainPage
from pages.new_repo_page import NewRepoPage
from pages.repo_page import RepoPage
from pages.search_page import SearchPage
from test_data import credentials
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def authorized_page(driver):
    page = LoginPage(driver)
    page.open(page.url)
    page.enter_login(credentials.valid_login)
    page.enter_password(credentials.valid_password)
    page.click_sign_in()
    page.home_title_is_displayed
    return page


@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver)
    page.open(page.url)
    return page


@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.open(page.url)
    return page


@pytest.fixture()
def search_page(driver):
    return SearchPage(driver)


@pytest.fixture()
def new_repo_page(driver, authorized_page):
    new_repo_page = NewRepoPage(driver)
    authorized_page.open(new_repo_page.url)
    new_repo_page.repository_name_input_is_displayed
    return new_repo_page


@pytest.fixture()
def repo_page(driver):
    return RepoPage(driver)


@pytest.fixture()
def create_repo(new_repo_page):
    new_repo_page.enter_repository_name(credentials.new_repo_name)
    new_repo_page.repo_name_available_label_is_displayed
    new_repo_page.click_create_repository_button()
    return new_repo_page


@pytest.fixture()
def delete_repo():
    yield
    response = requests.delete(
        f'https://api.github.com/repos/{credentials.valid_login}/{credentials.new_repo_name}',
        headers={
            'Authorization': f'Bearer {credentials.API_KEY}',
            'X-GitHub-Api-Version': '2022-11-28',
            'Accept': 'application/vnd.github+json'
        }
    )
    print('\nSTATUS CODE:', response.status_code)
    assert response.status_code == 204


@pytest.fixture()
def create_repo_endpoint():
    return CreateRepoEndpoint()


@pytest.fixture()
def get_repo_endpoint():
    return GetRepoEndpoint()


@pytest.fixture()
def create_repo_with_api(create_repo_endpoint):
    repository = Repository(
        name=f'{credentials.new_repo_name}',
        description='description'
    )
    response = create_repo_endpoint.create_repo(repository)
    assert response.status_code == 201
