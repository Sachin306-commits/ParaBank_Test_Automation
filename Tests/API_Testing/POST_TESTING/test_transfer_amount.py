from Payloads.common_payload import load_test_data, build_customer_payload
from api_clients.Post_API.trsnsfer_amount import post_transfer_amount


def test_post_transfer_amount():
    #  Load data from JSON file (returns dictionary)
    user_data = load_test_data()  # you can also pass an index if you want: load_test_data(0)

    #  Build the payload from the loaded data
    payload = build_customer_payload(user_data)

    #  Call API Client function
    response = post_transfer_amount(payload,fromAccount_Id=31659,toAccount_Id=31659, amount=122003.00)


    #  Debug + Assertion
    print("Status Code:", response.status_code)
    print("\nResponse Body:", response.text)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
