from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_select,safe_get_text
from selenium.webdriver.support.ui import Select

class saving_account:

    def __init__(self,driver):
        self.driver = driver

    def click_on_account(self):
        safe_click(self.driver,Locators.saving_account)
    def select_saving_account(self,SAVINGS):
        #select = Select(self.driver,SAVINGS)
        safe_select(self.driver,Locators.select_saving,SAVINGS)

        #select.select_by_visible_text("SAVINGS")
    def create_saving_account(self):
        safe_click(self.driver,Locators.create_account)

    def account_creation(self):
        return safe_get_text(self.driver,Locators.account_message)
    def account_creation_1(self):
        return safe_get_text(self.driver,Locators.account_message_1)
    def account_creation_2(self):
        return safe_get_text(self.driver,Locators.account_message_2)