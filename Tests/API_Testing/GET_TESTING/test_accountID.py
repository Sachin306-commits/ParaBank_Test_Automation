import requests
import pytest


def test_accountNumber():

    response = requests.get("https://parabank.parasoft.com/parabank/services/bank/accounts/20337")
    print(response.status_code)
    print(response.headers)
    if response.status_code == 200:
        print(" Your Account is find ")
    else:
        print("API Failed")