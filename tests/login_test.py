from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utils.urls import Urls


class LoginTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.url = Urls.LOGIN_URL
        self.driver.get(self.url)

    def test_login_to_app_without_captcha(self):
        self.login_page.accept_cookies()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_login_button()
        self.assertTrue(self.login_page.find_field_required())
