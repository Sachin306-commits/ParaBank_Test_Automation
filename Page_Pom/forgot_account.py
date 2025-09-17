from Utils.selenium_helpers import safe_click, safe_get_text, safe_send_keys
from Utils.locators import Locators

class forgot_account:
    def __init__(self,driver):
        self.driver = driver

    def click_on_forgot(self):
        safe_click(self.driver,Locators.forgot)

    def first_name(self,user_first_name):
        safe_send_keys(self.driver,Locators.first_name_1,user_first_name)

    def last_name(self,user_second_name):
        safe_send_keys(self.driver,Locators.last_name_1,user_second_name)

    def forgot_address(self,user_address):
        safe_send_keys(self.driver,Locators.forgot_address,user_address)

    def city(self,user_city):
        safe_send_keys(self.driver,Locators.forgot_city,user_city)

    def forgot_state(self,user_state):
        safe_send_keys(self.driver,Locators.forgot_state,user_state)

    def zip_code(self,user_zip_code):
        safe_send_keys(self.driver,Locators.forgot_zip_code,user_zip_code)

    def forgot_ssn(self,user_ssn):
        safe_send_keys(self.driver,Locators.forgot_ssn,user_ssn)

    def forgot_button(self):
        safe_click(self.driver,Locators.forgot_button)

    def right_panel(self):
       return safe_get_text(self.driver,Locators.Right_panel)