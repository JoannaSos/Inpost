from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from utils.urls import Urls


class Locators:
    BUTTON_ACCEPT_COOKIES = (By.ID, "onetrust-accept-btn-handler")


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = Urls.BASE_URL

    def click_when_element_is_clickable(self, locator):
        wait = WebDriverWait(self.driver, 40)
        elem = wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def locate_when_element_is_located(self, locator):
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.visibility_of_element_located(locator))
        return elem

    def accept_cookie(self):
        try:
            self.click_when_element_is_clickable(Locators.BUTTON_ACCEPT_COOKIES)
        except ElementClickInterceptedException:
            self.click_when_element_is_clickable(Locators.BUTTON_ACCEPT_COOKIES)
