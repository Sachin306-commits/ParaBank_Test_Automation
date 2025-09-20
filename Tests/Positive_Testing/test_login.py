import json
import time
import pytest
from Page_Pom.Positive_POM.login import Login_user


test_data_path = r'C:\Users\Sachin Kumar Tiwari\PycharmProjects\ParaBank_Testing\Data\test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

user_data = test_list[0]

@pytest.mark.smoke
def test_register_user(browserInstance):
    driver = browserInstance
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    browserInstance.maximize_window()
    Login_user_check =Login_user(browserInstance)
    Login_user_check.enter_login_name(user_data["user_name_1"])
    Login_user_check.enter_login_password(user_data["user_confirm_password"])
    Login_user_check.click_on_submit_button()
    time.sleep(4)

