import requests
import json

url = "http://127.0.0.1:8000/insert/"

data = {

    "id": 2,
    "student_name": "Monirul Islam II",
}

json_data = json.dumps(data)

r = requests.put(url= url, data = json_data)

data = r.json()
print(data)

