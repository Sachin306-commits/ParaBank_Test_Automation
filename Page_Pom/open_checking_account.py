from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_get_text,safe_send_keys,safe_select

class checking_Account:

    def __init__(self,driver):
        self.driver = driver

    def open_account(self):
        safe_click(self.driver,Locators.saving_account)

    def select_saving_account(self,selected=None):
        return safe_select(self.driver,Locators.select_saving,selected)

    def select_amount(self,selected=None):
        return safe_select(self.driver,Locators.money_selection,selected)

    def create_saving_account(self):
        safe_click(self.driver,Locators.create_account)

    def successfuly_message(self):
        return safe_get_text(self.driver,Locators.successfuly_checking_creation)

