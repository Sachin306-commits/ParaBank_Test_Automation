import requests
class RequestHandler:

    @staticmethod
    def send_post_request(url, params, headers, payload):
        response = requests.post(url, params=params, json=payload, headers=headers)
        return response

    @staticmethod
    def send_get_request(url, headers, params=None, payload=None):
        response = requests.get(url, headers=headers, params=params, json=payload)
        return response
    @staticmethod
    def send_put_request(url,headers,params = None,payload = None):
        response = requests.put(url,headers=headers,params=params,json=payload)
        return response