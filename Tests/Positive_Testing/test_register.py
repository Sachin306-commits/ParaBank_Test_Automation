import json
import time

import pytest
from Utils.locators import Locators
from Utils.selenium_helpers import safe_click, safe_get_text
from Page_Pom.Positive_POM.register import Register


test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\ParaBank_Testing\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]
expected_username = user_data["user_name_1"]


@pytest.mark.smoke
def test_register_user(browserInstance):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    registration = Register(browserInstance)
    registration.click_on_register_page()
    registration.first_name(user_data["user_first_name"])
    registration.last_name(user_data["user_second_name"])
    registration.address(user_data["user_address"])
    registration.city(user_data["user_city"])
    registration.state(user_data["user_state"])
    registration.zip_code(user_data["user_zip_code"])
    registration.phone(user_data["user_phone_no"])
    registration.ssn(user_data["user_ssn"])
    registration.user_name(user_data["user_name_1"])
    registration.password(user_data["user_password"])
    registration.confirm_password(user_data["user_confirm_password"])
    time.sleep(1)
    registration.click_register()
    time.sleep(4)
    # Build expected welcome text dynamically
    expected_text = f"Welcome {expected_username}\nYour account was created successfully. You are now logged in."

    # Assertion
    welcome_message = registration.welcome_note()
    assert welcome_message.strip() == expected_text.strip(), \
        f"Expected '{expected_text}' but got: '{welcome_message}'"


