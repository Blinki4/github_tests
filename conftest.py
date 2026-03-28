import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from services.repository.repositories_api_service import RepositoriesAPIService
from services.users.users_api_service import UsersAPIService
from pages.main_page import MainPage
from pages.new_repo_page import NewRepoPage
from pages.repo_page import RepoPage
from pages.search_page import SearchPage
from pages.login_page import LoginPage

load_dotenv()

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture()
def authorized_page(driver):
    page = LoginPage(driver)
    page.open(page.url)
    page.enter_login(os.getenv('LOGIN'))
    page.enter_password(os.getenv('PASSWORD'))
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
def repo_page(driver):
    return RepoPage(driver)

@pytest.fixture()
def new_repo_page(driver, authorized_page):
    new_repo_page = NewRepoPage(driver)
    authorized_page.open(new_repo_page.url)
    new_repo_page.repository_name_input_is_displayed
    return new_repo_page

@pytest.fixture()
def create_repository_ui(new_repo_page):
    new_repo_page.enter_repository_name(os.getenv('REPO_NAME'))
    new_repo_page.repo_name_available_label_is_displayed
    new_repo_page.click_create_repository_button()
    return new_repo_page

@pytest.fixture()
def repositories_api_service():
    return RepositoriesAPIService()

@pytest.fixture()
def users_api_service():
    return UsersAPIService()

@pytest.fixture()
def create_repository_req(repositories_api_service):
    new_repository = {
        'name': os.getenv('REPO_NAME'),
        'description': 'new_description'
    }
    repositories_api_service.create_repository(body=new_repository)

@pytest.fixture()
def delete_repository_req(repositories_api_service):
    yield
    repositories_api_service.delete_repository(
        owner=os.getenv('LOGIN'),
        repo=os.getenv('REPO_NAME')
    )