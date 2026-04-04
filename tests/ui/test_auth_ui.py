import os
import pytest
import allure
from dotenv import load_dotenv

load_dotenv()

@allure.epic('Авторизация через UI')
class TestAuthUI:

    @pytest.mark.ui
    @allure.title('Главная страница открывается после авторизации')
    def test_redirect_to_main_page_after_sign_in(self, authorized_page):
        assert authorized_page.home_title_is_displayed

    @pytest.mark.ui
    @allure.title('Проверка имени пользователя после авторизации')
    def test_sign_in(self, authorized_page):
        authorized_page.click_navbar_avatar()
        assert authorized_page.navigation_menu_username_text == os.getenv('LOGIN')

    @pytest.mark.ui
    @allure.title('Авторизация с неправильным паролем')
    def test_auth_with_invalid_password(self, login_page):
        login_page.enter_login(os.getenv('LOGIN'))
        login_page.enter_password('invalid')
        login_page.click_sign_in()
        assert login_page.error_text == 'Incorrect username or password.'

    @pytest.mark.ui
    @allure.title('Пароль скрыт')
    def test_password_is_hidden(self, login_page):
        assert login_page.password_is_hidden

    @pytest.mark.ui
    @allure.title('Логин имеет аттрибут required')
    def test_login_required(self, login_page):
        assert login_page.login_is_required


    @pytest.mark.ui
    @allure.title('Логин не валидирован')
    def test_login_validated(self, login_page):
        assert not login_page.login_is_validated


    @pytest.mark.ui
    @allure.title('Пароль имеет аттрибут required')
    def test_password_required(self, login_page):
        assert login_page.password_is_required


    @pytest.mark.ui
    @allure.title('Пароль не валидирован')
    def test_password_validated(self, login_page):
        assert not login_page.password_is_validated


    @pytest.mark.ui
    @allure.title('Переход на страницу "Забыли пароль"')
    def test_redirect_to_forgot_password(self, login_page):
        login_page.click_forgot_password_link()
        assert login_page.current_url == 'https://github.com/password_reset'

    @pytest.mark.ui
    @allure.title('Переход на страницу "Регистрация"')
    def test_redirect_to_sign_up(self, login_page):
        login_page.click_create_account_link()
        assert login_page.current_url == 'https://github.com/signup?source=login'

    @pytest.mark.ui
    @allure.title('Вход с пустой формой')
    def test_empty_form_sign_in(self, login_page):
        login_page.click_sign_in()
        assert login_page.current_url == 'https://github.com/login'