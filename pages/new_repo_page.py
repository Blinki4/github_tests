import allure

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class NewRepoPage(BasePage):
    url = 'https://github.com/new'
    repository_name_input_selector = (By.ID, 'repository-name-input')
    create_repository_button_selector = (By.XPATH, '//button/following::*[text()="Create repository"]')
    repo_name_available_label_selector = (By.ID, 'RepoNameInput-is-available')
    repo_name_message_label_selector = (By.ID, 'RepoNameInput-message')
    visibility_select_selector = (By.ID, 'visibility-anchor-button')
    private_option_selector = (By.XPATH, '//*[text()="You choose who can see and commit to this repository."]')

    def __init__(self, driver):
        super().__init__(driver)


    @property
    def repository_name_input(self):
        return self.find(self.repository_name_input_selector)


    @property
    def repository_name_input_is_displayed(self):
        return self.repository_name_input.is_displayed()


    @allure.step('Ввод названия репозитория')
    def enter_repository_name(self, value):
        self.repository_name_input.send_keys(value)


    @property
    def create_repository_button(self):
        return self.find(self.create_repository_button_selector)


    @allure.step('Создать репозиторий')
    def click_create_repository_button(self):
        self.create_repository_button.click()


    @property
    def repo_name_available_label(self):
        return self.wait_element(EC.visibility_of_element_located(self.repo_name_available_label_selector))


    @property
    def repo_name_available_label_is_displayed(self):
        return self.repo_name_available_label.is_displayed()


    @property
    def repo_name_message_label(self):
        return self.wait_element(EC.visibility_of_element_located(self.repo_name_message_label_selector))


    @property
    def repo_name_message_label_text(self):
        return self.repo_name_message_label.text


    @property
    def repo_name_message_label_is_displayed(self):
        return self.repo_name_message_label.is_displayed()


    @property
    def visibility_select(self):
        return self.find(self.visibility_select_selector)


    @allure.step('Открыть селект приватности репозитория')
    def click_visibility_select(self):
        self.visibility_select.click()


    @property
    def private_option(self):
        return self.wait_element(EC.element_to_be_clickable(self.private_option_selector))


    @allure.step('Выбрать приватный репозиторий')
    def click_private_option(self):
        self.private_option.click()