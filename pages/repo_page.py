import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RepoPage(BasePage):
    repo_title_selector = (By.XPATH, '//strong[@itemprop="name"]')

    def __init__(self, driver):
        super().__init__(driver)


    @property
    def repo_title(self):
        return self.wait_element(EC.visibility_of_element_located(self.repo_title_selector))


    @property
    def repo_title_text(self):
        return self.repo_title.text