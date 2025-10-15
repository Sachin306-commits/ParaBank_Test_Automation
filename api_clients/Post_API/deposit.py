from API_Helpers.params import deposit_params
from API_Helpers.URL import deposit_url
from API_Helpers.headers import headers_
from API_Helpers.response import send_post_request   #

def bill_pay_response(payload, account_id, amount):
    """Calls the bill pay API"""
    url = deposit_url()
    params = deposit_params(account_id, amount)
    headers_call = headers_()

    # Use the reusable response function
    response = send_post_request(url, params, headers_call, payload)
    return response
