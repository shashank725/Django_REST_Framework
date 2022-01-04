import json
import requests

# # To GET data
# URL = "http://127.0.0.1:8000/student-list/"
# req = requests.get(url=URL)
# data = req.json()
# print(data)



# To get secific/all tudent detail with Create and Update
URL = "http://127.0.0.1:8000/student-api/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    req = requests.get(url=URL, data=json_data)
    data = req.json()
    print(data)
get_data()

def post_data():
    data = {
        'name' : 'Rajat',
        'roll' : '104',
        'city' : 'Banaras'
    }
    json_data = json.dumps(data)
    req = requests.post(url=URL, data=json_data)
    data = req.json()
    print(data)
# post_data()

def update_data():
    data = {
        'id' : 5,
        'name' : 'Ankush',
    }
    json_data = json.dumps(data)
    req = requests.put(url=URL, data=json_data)
    data = req.json()
    print(data)
# update_data()

def delete_data():
    data = {'id':4}
    json_data = json.dumps(data)
    req = requests.delete(url=URL, data=json_data)
    data = req.json()
    print(data)
# delete_data()






# # To CREATE data (POST)
# URL = "http://127.0.0.1:8000/student-create/"
# data = {
#     'name' : 'Raj',
#     'roll' : '103',
#     'city' : 'Ranchi'
# }
# json_data = json.dumps(data)
# req = requests.post(url=URL, data=json_data)
# data = req.json()
# print(data)
 

