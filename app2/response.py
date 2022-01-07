import json
import requests

# To get secific/all tudent detail with Create and Update
URL = "http://127.0.0.1:8000/api/hello"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    req = requests.get(url=URL, data=json_data)
    data = req.json()
    print(data)
# get_data()

def post_data():
    data = {
        'name' : 'mohit',
        'roll' : '104',
        'city' : 'Banaras'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    req = requests.post(url=URL, headers=headers, data=json_data)
    data = req.json()
    print(data)
post_data()

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