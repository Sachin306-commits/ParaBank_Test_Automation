def send_post_request(url, params, headers, payload):
    """
    Generic reusable POST request function.
    """
    import requests
    response = requests.post(url, params=params, json=payload, headers=headers)
    return response
