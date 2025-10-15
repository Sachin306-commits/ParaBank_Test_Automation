import requests

def test_transaction():

    url = "https://parabank.parasoft.com/parabank/services/bank/accounts/128007/transactions"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("\n--- Raw XML Response ---")
    print(response.text)
    print(response.status_code)
