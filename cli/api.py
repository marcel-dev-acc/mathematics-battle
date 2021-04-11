import requests
import json

def create_session():
    params = {
        
    }
    r = requests.post('http://localhost:3011/api/create_session', data=params)
    print(r.status_code)
    print(r.text)

def add_user_to_session():
    params = json.dumps({
        'username': 'TestUser'
    })
    r = requests.put(url='http://localhost:3011/api/session/4d14ab03-1e1e-4a1c-a869-7f54fe6f5862/user', data=params)
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    add_user_to_session()