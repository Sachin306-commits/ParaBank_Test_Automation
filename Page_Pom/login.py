from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys
from Utils.locators import Locators

class Login_user:
    def __init__(self, driver):
        self.driver = driver

    def enter_login_name(self,user_name_1):
        safe_send_keys(self.driver,Locators.login_username,user_name_1)
    def enter_login_password(self,user_confirm_password):
        safe_send_keys(self.driver,Locators.login_password,user_confirm_password)
    def click_on_submit_button(self):
        safe_click(self.driver,Locators.login_submit)
