import requests
from API_Helpers.URL import transfer_amount_url
from API_Helpers.params import transfer_amount_params
from API_Helpers.headers import headers_
from API_Helpers.response import send_post_request


def post_transfer_amount(payload, fromAccount_Id,toAccount_Id, amount):
    """Sends the Bill Pay POST request"""
    url = transfer_amount_url()
    params = transfer_amount_params(fromAccount_Id, toAccount_Id,amount)
    headers_call = headers_()

    response = send_post_request(url, params, headers_call, payload)
    return response
