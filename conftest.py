import pytest

from pages.main_page import MainPage
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
    page = SearchPage(driver)
    return page