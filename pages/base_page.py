from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import Urls


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.url = Urls.BASE_URL

    def click_when_element_is_clickable(self, locator):
        wait = WebDriverWait(self.driver, 20)
        elem = wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def locate_when_element_is_located(self, locator):
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.visibility_of_element_located(locator))
        return elem

    # def get_current_url(self):
    #     return self.driver.current_url
