import allure

from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    results_titles_selector = (By.CSS_SELECTOR, '.search-title')


    def __init__(self, driver):
        super().__init__(driver)


    @property
    def results_titles(self):
        return self.wait_element(EC.visibility_of_all_elements_located(self.results_titles_selector))


    @allure.step('В результатах поиска есть нужное значение')
    def is_title_in_results(self, value):
        found = False
        for title in self.results_titles:
            if title.text == value:
                found = True
        return found