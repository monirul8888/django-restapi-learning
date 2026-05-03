import requests
import json
url = "http://127.0.0.1:8000/insert/"

data = {
    "id": 3,
    "student_name": "Akib",
    "student_id":221002177,
    "student_dept": "BBA"
}

json_data = json.dumps(data)

r = requests.put(url=url, data = json_data)

data = r.json()

print(data)

