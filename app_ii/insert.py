import requests
import json


url = "http://127.0.0.1:8000/insert/"

response = requests.get(url=url)

data = {
    "student_name": "Monirul Islam",
    "student_id": 221002154,
    "student_dept": "BBA"
}

json_data = json.dumps(data)

r = requests.post(url=url, data = json_data)

data = r.json()

print(data)

