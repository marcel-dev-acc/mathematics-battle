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
    session_id = 'e54cf233-6048-4487-b2bb-eff7cb491db2'
    r = requests.put(
        url='http://localhost:3011/api/session/{}/user'.format(
            session_id
        ), 
        data=params
    )
    print(r.status_code)
    print(r.text)

def get_new_problem():
    # params = json.dumps({
    #     'username': 'TestUser'
    # })
    session_id = 'e54cf233-6048-4487-b2bb-eff7cb491db2'
    username = 'TestUser'
    r = requests.get(
        url='http://localhost:3011/api/session/{}/user/{}/problem'.format(
            session_id,
            username
        ), 
        # data=params
    )
    print(r.status_code)
    print(r.text)

def submit_problem_solution():
    params = json.dumps({
        'problem_id': '4',
        'answer': '105'
    })
    session_id = 'e54cf233-6048-4487-b2bb-eff7cb491db2'
    username = 'TestUser'
    r = requests.post(
        url='http://localhost:3011/api/session/{}/user/{}/solution'.format(
            session_id,
            username
        ), 
        data=params
    )
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    submit_problem_solution()