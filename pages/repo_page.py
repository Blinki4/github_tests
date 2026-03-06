import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RepoPage(BasePage):
    repo_title_selector = (By.XPATH, '//strong[@itemprop="name"]')
    settings_tab_selector = (By.XPATH, '//*[@data-content="Settings"]')
    delete_repo_button_selector = (By.ID, 'repo-delete-proceed-button')
    proceed_input_selector = (By.XPATH, '//input[@data-test-selector="repo-delete-proceed-confirmation"]')
    delete_notification_selector = (By.CSS_SELECTOR, '.js-flash-alert')


    def __init__(self, driver):
        super().__init__(driver)


    @property
    def repo_title(self):
        return self.wait_element(EC.visibility_of_element_located(self.repo_title_selector))


    @property
    def repo_title_text(self):
        return self.repo_title.text


    @property
    def settings_tab(self):
        return self.find(self.settings_tab_selector)


    def click_settings(self):
        self.settings_tab.click()


    @property
    def delete_repo_button(self):
        return self.wait_element(EC.element_to_be_clickable(self.delete_repo_button_selector))


    def click_delete_repo_button(self):
        self.delete_repo_button.click()


    @property
    def proceed_input(self):
        return self.wait_element(EC.element_to_be_clickable(self.proceed_input_selector))


    def enter_proceed_input(self, value):
        self.proceed_input.send_keys(value)


    @property
    def delete_notification(self):
        return self.find(self.delete_notification_selector)


    @property
    def delete_notification_id_displayed(self):
        return self.delete_notification.is_displayed()