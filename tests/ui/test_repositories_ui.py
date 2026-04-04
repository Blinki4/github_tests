import os
import pytest
import allure
from dotenv import load_dotenv

load_dotenv()

@allure.epic('Тестирование репозиториев через UI')
class TestRepositoryUI:
    @pytest.mark.ui
    @allure.title('Переход на страницу нового репозитория')
    def test_redirect_to_new_repo_page(self, create_repository_ui, new_repo_page, delete_repository_req):
        assert new_repo_page.wait_url_to_be(f'https://github.com/Blinki4/{os.getenv('REPO_NAME')}')


    @pytest.mark.ui
    @allure.title('Проверка названия нового репозитория после создания')
    def test_new_repo_title_displayed(self, create_repository_ui, repo_page, delete_repository_req):
        assert repo_page.repo_title_text == os.getenv('REPO_NAME')


    @pytest.mark.ui
    @allure.title('Создание нового репозитория с существующим именем')
    def test_new_repo_with_existing_name(self, new_repo_page):
        new_repo_page.enter_repository_name('github_tests')
        assert new_repo_page.repo_name_message_label_text == 'github_tests already exists in this account'


    @pytest.mark.ui
    @allure.title('Создание приватного репозитория')
    def test_new_private_repo(self, new_repo_page, repo_page, delete_repository_req):
        new_repo_page.enter_repository_name(os.getenv('REPO_NAME'))
        new_repo_page.repo_name_available_label_is_displayed
        new_repo_page.click_visibility_select()
        new_repo_page.click_private_option()
        new_repo_page.click_create_repository_button()
        assert repo_page.repo_title_text == os.getenv('REPO_NAME')

    @pytest.mark.ui
    @allure.title('Удаление репозитория')
    def test_delete_repo(self, create_repository_ui, repo_page):
        repo_page.click_settings()
        repo_page.scroll_page_to_bottom()
        repo_page.click_start_delete_repo_button()
        repo_page.click_delete_repo_button()
        repo_page.click_delete_repo_button()
        repo_page.enter_proceed_input(f'{os.getenv('LOGIN')}/{os.getenv('REPO_NAME')}')
        repo_page.click_delete_repo_button()
        assert repo_page.delete_notification_id_displayed