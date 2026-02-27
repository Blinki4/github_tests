import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import credentials
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    time.sleep(2)
    driver.quit()


@pytest.fixture()
def authorized_page(driver):
    page = LoginPage(driver)
    page.open(page.url)
    page.enter_login(credentials.valid_login)
    page.enter_password(credentials.valid_password)
    page.click_sign_in()
    return page