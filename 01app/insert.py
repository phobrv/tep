import requests
import json

url = "http://127.0.0.1:8000/api/insertImage"

headers = {
    'Content-Type': 'application/json'
}


def insert(payload):
    response = requests.request("POST", url, headers=headers, data=payload, allow_redirects=False)
    print(response.text)
