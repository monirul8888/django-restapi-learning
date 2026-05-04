import requests
import json


url = "http://127.0.0.1:8000/insert/"

response = requests.get(url=url)

data = response.json()

print(data)