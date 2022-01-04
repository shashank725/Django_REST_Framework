import json
import requests

# # To GET data
# URL = "http://127.0.0.1:8000/student-list/"
# req = requests.get(url=URL)
# data = req.json()
# print(data)


# # To CREATE data (POST)
URL = "http://127.0.0.1:8000/student-create/"
data = {
    'name' : 'Raj',
    'roll' : '103',
    'city' : 'Ranchi'
}
json_data = json.dumps(data)
req = requests.post(url=URL, data=json_data)
data = req.json()
print(data)


