from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def open(self, url: str):
        self.driver.get(url)


    def find(self, args):
        return self.driver.find_element(*args)


    def find_several(self, args):
        return self.driver.find_elements(*args)


    def wait_element(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            condition
        )


    @property
    def current_url(self):
        return self.driver.current_url


    def wait_url_to_be(self, url: str, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )