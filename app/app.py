import requests, json

ur = "http://127.0.0.1:8000/insert/"

data = {

    "student_name": "Monirul",
    "student_id": 221002157,
    "student_dept": "CSE"
}

json_data = json.dumps(data)

r = requests.post(url= ur, data = json_data)

data = r.json()
print(data)