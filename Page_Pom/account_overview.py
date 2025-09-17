from Utils.locators import Locators
from Utils.selenium_helpers import safe_click,safe_select,safe_get_text,safe_send_keys

class account_overview:

    def __init__(self,driver):
        self.driver = driver
    def click_on_overview(self):
        safe_click(self.driver,Locators.overview)
    def account_overview(self):
        return safe_get_text(self.driver,Locators.tittle_compare)
