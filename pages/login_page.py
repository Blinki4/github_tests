import allure
from test_data import credentials

from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    url = 'https://github.com/login'
    login_input_selector = (By.ID, 'login_field')
    password_input_selector = (By.ID, 'password')
    sign_in_button_selector = (By.XPATH, '//input[@value="Sign in"]')
    home_title_selector = (By.XPATH, '//h2[text()="Home"]')
    navbar_avatar_selector = (By.XPATH, '//img[@data-testid="github-avatar"]')
    navigation_menu_username_selector = (By.XPATH, f'//div[@title="{credentials.valid_login}"]')
    error_selector = (By.CSS_SELECTOR, '.js-flash-alert')
    forgot_password_link_selector = (By.ID, 'forgot-password')
    create_account_link_selector = (By.LINK_TEXT, 'Create an account')


    def __init__(self, driver):
        super().__init__(driver)


    @property
    def login_input(self):
        return self.find(self.login_input_selector)


    @allure.step('Ввод логина')
    def enter_login(self, value: str):
        self.login_input.send_keys(value)


    @property
    def login_is_required(self):
        return self.login_input.get_attribute('required') == 'true'


    @property
    def login_is_validated(self):
        return self.driver.execute_script(
            'return arguments[0].checkValidity()',
            self.login_input
        )


    @property
    def password_input(self):
        return self.find(self.password_input_selector)


    @allure.step('Ввод пароля')
    def enter_password(self, value: str):
        self.password_input.send_keys(value)


    @property
    def password_is_hidden(self):
        return self.password_input.get_attribute('type') == 'password'


    @property
    def password_is_required(self):
        return self.password_input.get_attribute('required') == 'true'


    @property
    def password_is_validated(self):
        return self.driver.execute_script(
            'return arguments[0].checkValidity()',
            self.password_input
        )


    @property
    def sign_in_button(self):
        return self.find(self.sign_in_button_selector)


    @allure.step('Войти')
    def click_sign_in(self):
        self.sign_in_button.click()


    @property
    def home_title(self):
        return self.wait_element(EC.visibility_of_element_located(self.home_title_selector))


    @property
    def home_title_is_displayed(self):
        return self.home_title.is_displayed()


    @property
    def navbar_avatar(self):
        return self.wait_element(EC.element_to_be_clickable(self.navbar_avatar_selector))


    @allure.step('Кликнуть на аватар')
    def click_navbar_avatar(self):
        self.navbar_avatar.click()


    @property
    def navigation_menu_username(self):
        return self.wait_element(EC.visibility_of_element_located(self.navigation_menu_username_selector))


    @property
    def navigation_menu_username_text(self):
        return self.navigation_menu_username.text


    @property
    def error(self):
        return self.wait_element(EC.visibility_of_element_located(self.error_selector))


    @property
    def error_text(self):
        return self.error.text.strip().split('"')[0]


    @property
    def forgot_password_link(self):
        return self.find(self.forgot_password_link_selector)


    @allure.step('Кликнуть "Forgot password"')
    def click_forgot_password_link(self):
        self.forgot_password_link.click()


    @property
    def create_account_link(self):
        return self.find(self.create_account_link_selector)


    @allure.step('Кликнуть "Create an account"')
    def click_create_account_link(self):
        self.create_account_link.click()