import os

from selenium.webdriver.common.by import By

import data.data
import data.expected_result
from pages.base_page import BasePage


class Locators:
    INPUT_LOGIN = (By.XPATH, "//input[@id='input_login']")
    INPUT_PASSWORD = (By.XPATH, "//input[@id='input_password']")
    BUTTON_LOGIN = (By.ID, "submit_submit")
    # BUTTON_ACCEPT_COOKIES = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/button")
    FIELD_REQUIRED = (By.XPATH, "//li[contains(text(),'Pole wymagane')]")


class LoginPage(BasePage):

    def enter_login(self):
        USER = os.getenv(data.data.USER)
        self.locate_when_element_is_located(Locators.INPUT_LOGIN).send_keys(USER)

    def enter_password(self):
        PASSWORD = os.environ.get(data.data.PASSWORD)
        self.driver.find_element(*Locators.INPUT_PASSWORD).send_keys(PASSWORD)

    def click_login_button(self):
        self.driver.find_element(*Locators.BUTTON_LOGIN).click()

    def accept_cookies(self):
        self.accept_cookie()

    def find_field_required(self):
        field_required = self.locate_when_element_is_located(Locators.FIELD_REQUIRED).text
        field_required_text = data.expected_result.Results.field_required_text
        if field_required not in field_required_text:
            return False
        else:
            return True
