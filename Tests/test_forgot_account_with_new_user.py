from Page_Pom.forgot_account import forgot_account
from Page_Pom.forgot_account_with_new_user import forgot_new_account
import pytest
import json
import time
test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\ParaBank_Testing\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]

@pytest.mark.smoke
def test_forgot_account(browserInstance):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    user_forgot_network = forgot_account(browserInstance)
    user_forgot_network.click_on_forgot()
    user_forgot_network.first_name(user_data["user_first_name"])
    user_forgot_network.last_name(user_data["user_second_name"])
    user_forgot_network.forgot_address(user_data["user_address"])
    user_forgot_network.city(user_data["user_city"])
    user_forgot_network.forgot_state(user_data["user_state"])
    user_forgot_network.zip_code(user_data["user_zip_code"])
    user_forgot_network.forgot_ssn(user_data["user_ssn"])
    user_forgot_network.forgot_button()
    time.sleep(3)
    error_check_with_new_user = forgot_new_account(browserInstance)
    error_message = error_check_with_new_user.account_check()
    display_error_message = f"Error!\nThe customer information provided could not be found."
    error_message.strip() == display_error_message.strip(), \
            f"Expected '{error_message}' but got: '{display_error_message}'"

