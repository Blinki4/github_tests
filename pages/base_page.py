from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def open(self, url: str):
        self.driver.get(url)


    def find(self, args):
        return self.driver.find_element(*args)


    def wait_element(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            condition
        )