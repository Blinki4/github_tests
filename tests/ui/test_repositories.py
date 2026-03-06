import time
import pytest
import allure

from selenium.webdriver.common.by import By
from test_data import credentials
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
@allure.title('Переход на страницу нового репозитория')
def test_redirect_to_new_repo_page(create_repo, delete_repo):
    assert create_repo.wait_url_to_be(f'https://github.com/Blinki4/{credentials.new_repo_name}')


@pytest.mark.ui
@allure.title('Проверка названия нового репозитория после создания')
def test_new_repo_title_displayed(create_repo, repo_page, delete_repo):
    assert repo_page.repo_title_text == credentials.new_repo_name


@pytest.mark.ui
@allure.title('Создание нового репозитория с существующим именем')
def test_new_repo_with_existing_name(new_repo_page):
    new_repo_page.enter_repository_name('github_tests')
    assert new_repo_page.repo_name_message_label_text == 'github_tests already exists in this account'


@pytest.mark.ui
@allure.title('Создание приватного репозитория')
def test_new_private_repo(new_repo_page, repo_page, delete_repo):
    new_repo_page.enter_repository_name(credentials.new_repo_name)
    new_repo_page.repo_name_available_label_is_displayed
    new_repo_page.click_visibility_select()
    new_repo_page.click_private_option()
    new_repo_page.click_create_repository_button()
    assert repo_page.repo_title_text == credentials.new_repo_name



@pytest.mark.ui
@allure.title('Удаление репозитория')
def test_delete_repo(create_repo, repo_page, delete_repo):
    repo_page.find((By.XPATH, '//*[@data-content="Settings"]')).click()
    time.sleep(5)
    repo_page.driver.execute_script(
        'window.scrollTo(0, 100000)',
        repo_page.find((By.CSS_SELECTOR, 'html'))
    )
    time.sleep(5)