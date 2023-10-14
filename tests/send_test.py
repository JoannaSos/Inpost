import time
from pages.send_page import SendPage
from tests.base_test import BaseTest
from utils.urls import Urls


class SendTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.send_page = SendPage(self.driver)
        self.url = Urls.BASE_URL
        self.driver.get(self.url)

    def test_choose_sending_packed(self):
        self.send_page.accept_cookies()
        self.send_page.choose_type_of_sending()
        self.send_page.choose_size_of_packed()
        self.send_page.enter_data_of_customer()
        self.send_page.enter_data_of_sender()
        self.send_page.accept_agreement()
        self.send_page.click_button_send()
        self.assertTrue(self.send_page.find_summary)
        time.sleep(5)


