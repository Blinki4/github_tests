import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class MainPage(BasePage):
    url = 'https://github.com/'
    input_button_selector = (By.CSS_SELECTOR, '.input-button')
    search_input_selector = (By.ID, 'query-builder-test')


    def __init__(self, driver):
        super().__init__(driver)


    @property
    def input_button(self):
        return self.find(self.input_button_selector)


    def open_search(self):
        self.input_button.click()


    @property
    def search_input(self):
        return self.wait_element(EC.element_to_be_clickable(self.search_input_selector))


    @allure.step('Ввести значение в поиск')
    def enter_search_input(self, value):
        return self.search_input.send_keys(value)