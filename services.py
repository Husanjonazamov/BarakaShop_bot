import requests
from utils.env import BASE_URL

def createUser(user):
    url = f"{BASE_URL}/users/"
    response = requests.post(url, json=user)
    
    if response.status_code == 201:  
        data = response.json()
        return data
    else:
        print(response.status_code)


def getUser(user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.get(url)  
    
    if response.status_code == 200: 
        data = response.json()
        return data
    else:
        print(response.status_code)


def putName(user_id, name):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.put(url, data={'name': name})
    print(response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)
        
        
        
def putPhone(user_id, phone):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.put(url, data={'phone': phone})
    print(response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)
    
    

def getAbout():
    url = f"{BASE_URL}/about/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)
        

def getOrder(user_id):
    url = f"{BASE_URL}/order/{user_id}"
    response = requests.get(url)
    print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        return data 
    else:
        print(response.status_code)    