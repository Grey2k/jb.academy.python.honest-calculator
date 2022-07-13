import requests
from requests.exceptions import InvalidSchema


def get_response(url):
    try:
        response = requests.get(url)
        print(response.status_code)
    except InvalidSchema:
        print('No response')
