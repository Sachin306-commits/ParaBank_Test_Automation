from Payloads.common_payload import load_test_data, build_customer_payload
from api_clients.Post_API.bill_pay import bill_pay_response

def test_bill_pay():
    user_data = load_test_data()
    payload = build_customer_payload(user_data)

    response = bill_pay_response(payload, account_id=15342, amount=100000.00)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
