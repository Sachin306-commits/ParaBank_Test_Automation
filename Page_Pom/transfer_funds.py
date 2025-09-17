from Utils.locators import Locators
from Utils.selenium_helpers import safe_select,safe_click,safe_get_text,safe_send_keys
from selenium.webdriver.support.ui import Select

class transfer:
    def __init__(self,driver):
        self.driver = driver

    def click_on_transfer_button(self):
        safe_click(self.driver,Locators.click_on_transfer)

    def money_transfer(self,send_money):
        safe_send_keys(self.driver,Locators.transfer_funds,send_money)

    def from_account(self, selected=None):
        return safe_select(self.driver, Locators.from_bank, selected)
        #return safe_select(self.driver, Locators.to_bank, value=1, by="index") if i want to select the second option from the dropdown.

    def to_account(self, selected=None):
        return safe_select(self.driver, Locators.to_bank, selected)

    def click_on_transfer(self):
        safe_click(self.driver,Locators.transfer_money_button)

    def transfer_message_show(self):
        return safe_get_text(self.driver,Locators.transfer_completion_message)

