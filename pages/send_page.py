from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

import data.data
import data.expected_result
from pages.base_page import BasePage


class Locators:
    # BUTTON_ACCEPT_COOKIES = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/button")
    BUTTON_SEND_PACKAGE = (
        By.XPATH, "/html/body/div[2]/div/div/div/main/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/a")
    BUTTON_SEND = (By.XPATH,
                   "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/div[2]/button")
    BOX_SEND_FROM_PACZKOMAT_TO_PACZKOMAT = (By.XPATH,
                                            "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/app-dynamic-form/form/app-section[1]/div/app-input[2]/div/div/div/app-input-radio/span[1]/label")
    CHECKBOX_MIDDLE_PACKAGE = (By.XPATH,
                               "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/app-dynamic-form/form/app-section[2]/div/app-input[2]/div/div/div/app-input-radio/span[2]")
    NAME_AND_SURNAME_OF_THE_RECIPIENT = (By.XPATH,
                                         "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/app-dynamic-form/form/app-section[4]/div/app-input/div/div/div/app-input-text/input")
    NAME_AND_SURNAME_OF_THE_SENDER = (By.XPATH,
                                      "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/app-dynamic-form/form/app-section[9]/div/app-input/div/div/div/app-input-text/input")
    E_MAIL_OF_THE_RECIPIENT = (By.XPATH,
                               "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/app-dynamic-form/form/app-section[5]/div/app-input/div/div/div/app-input-text/input")
    E_MAIL_OF_THE_SENDER = (By.XPATH,
                            "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/app-dynamic-form/form/app-section[10]/div/app-input/div/div/div/app-input-text/input")
    PHONE_NUMBER_OF_THE_RECIPIENT = (By.XPATH,
                                     "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/app-dynamic-form/form/app-section[6]/div/app-input/div/div/div/app-input-text/input")
    PHONE_NUMBER_OF_THE_SENDER = (By.XPATH,
                                  "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/app-dynamic-form/form/app-section[11]/div/app-input/div/div/div/app-input-text/input")
    ADDRESS_PACZKOMAT_OF_THE_RECIPIENT_SECTION = (By.XPATH,
                                                  "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/app-dynamic-form/form/app-section[7]/div/app-input/div[1]/div/div/app-points-select/ng-select/div/div/div[2]/input")
    ADDRESS_PACZKOMAT_OF_THE_RECIPIENT_FROM_THE_LIST = (
        By.XPATH, "//div[contains(text(),'Nowy Świat 42, 86-170 Nowe')]")
    AGREEMENT_CHECKBOX = (By.XPATH,
                          "/html/body/app-root/app-public-layout/div/div[2]/app-home/section/div[2]/div[4]/div/app-parcel-form/div/div/div[1]/app-dynamic-form/form/app-section[15]/div/app-input[2]/div/div/div/app-input-checkbox/div")
    SUMMARY_TEXT = (By.XPATH, "//h4[contains(text(),'Podsumowanie')]")


class SendPage(BasePage):

    def button_send_package(self):
        click_send_package = self.driver.find_element(*Locators.BUTTON_SEND_PACKAGE)
        click_send_package.click()

    def accept_cookies(self):
        self.accept_cookie()

    def choose_type_of_sending(self):
        self.click_when_element_is_clickable(Locators.BOX_SEND_FROM_PACZKOMAT_TO_PACZKOMAT)

    def choose_size_of_package(self):
        try:
            self.click_when_element_is_clickable(Locators.CHECKBOX_MIDDLE_PACKAGE)
        except ElementClickInterceptedException:
            self.click_when_element_is_clickable(Locators.CHECKBOX_MIDDLE_PACKAGE)

    def enter_data_of_customer(self):
        self.driver.find_element(*Locators.NAME_AND_SURNAME_OF_THE_RECIPIENT).send_keys(
            data.data.NAME_AND_SURNAME_OF_THE_RECIPIENT)
        self.driver.find_element(*Locators.E_MAIL_OF_THE_RECIPIENT).send_keys(data.data.E_MAIL_OF_THE_RECIPIENT)
        self.driver.find_element(*Locators.PHONE_NUMBER_OF_THE_RECIPIENT).send_keys(
            data.data.PHONE_NUMBER_OF_THE_RECIPIENT)
        self.driver.find_element(*Locators.ADDRESS_PACZKOMAT_OF_THE_RECIPIENT_SECTION).send_keys(
            data.data.ADDRESS_PACZKOMAT_OF_THE_RECIPIENT_SECTION)
        self.click_when_element_is_clickable(Locators.ADDRESS_PACZKOMAT_OF_THE_RECIPIENT_FROM_THE_LIST)

    def enter_data_of_sender(self):
        self.driver.find_element(*Locators.NAME_AND_SURNAME_OF_THE_SENDER).send_keys(
            data.data.NAME_AND_SURNAME_OF_THE_SENDER)
        self.driver.find_element(*Locators.E_MAIL_OF_THE_SENDER).send_keys(data.data.E_MAIL_OF_THE_SENDER)
        self.driver.find_element(*Locators.PHONE_NUMBER_OF_THE_SENDER).send_keys(data.data.PHONE_NUMBER_OF_THE_SENDER)

    def accept_agreement(self):
        try:
            self.driver.find_element(*Locators.AGREEMENT_CHECKBOX).click()
        except ElementClickInterceptedException:
            self.driver.find_element(*Locators.AGREEMENT_CHECKBOX).click()

    def click_button_send(self):
        try:
            self.driver.find_element(*Locators.BUTTON_SEND).click()
        except ElementClickInterceptedException:
            self.driver.find_element(*Locators.BUTTON_SEND).click()

    def find_summary(self):
        summary = self.locate_when_element_is_located(Locators.SUMMARY_TEXT).text
        summary_text = data.expected_result.Results.summary_text
        if summary not in summary_text:
            print(summary)
            return False
        else:
            return True
