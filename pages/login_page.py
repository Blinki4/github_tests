import allure
import credentials

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


    def __init__(self, driver):
        super().__init__(driver)


    @property
    def login_input(self):
        return self.find(self.login_input_selector)


    def enter_login(self, value: str):
        self.login_input.send_keys(value)


    @property
    def password_input(self):
        return self.find(self.password_input_selector)


    def enter_password(self, value: str):
        self.password_input.send_keys(value)


    @property
    def sign_in_button(self):
        return self.find(self.sign_in_button_selector)


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


    def click_navbar_avatar(self):
        self.navbar_avatar.click()


    @property
    def navigation_menu_username(self):
        return self.wait_element(EC.visibility_of_element_located(self.navigation_menu_username_selector))


    @property
    def navigation_menu_username_text(self):
        return self.navigation_menu_username.text