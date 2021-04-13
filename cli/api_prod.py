import requests
import json
import pytest

BASE_URL = 'http://localhost:1350'

def create_session():
    params = {}
    r = requests.post(BASE_URL + '/api/create_session', data=params)
    print(r.status_code)
    assert r.status_code == 200
    # print(r.json())
    return r.json() if r.status_code == 200 else None

def add_user_to_session(session_id=None):
    if not session_id:
        session = create_session()
        session_id = session.get('data').get('session_id')
    params = json.dumps({
        'username': 'TestUser'
    })
    r = requests.put(
        url=BASE_URL + '/api/session/{}/user'.format(
            session_id
        ), 
        data=params
    )
    print(r.status_code)
    # print(r.text)
    assert r.status_code == 200
    return r.json() if r.status_code == 200 else None

def get_new_problem(session_id=None, username=None):
    if not session_id or not username:
        session = create_session()
        session_id = session.get('data').get('session_id')
        add_user_to_session(session_id)
        username = 'TestUser'
    r = requests.get(
        url=BASE_URL + '/api/session/{}/user/{}/problem'.format(
            session_id,
            username
        ), 
        # data=params
    )
    print(r.status_code)
    assert r.status_code == 200
    # print(r.text)
    return r.json() if r.status_code == 200 else None

def submit_problem_solution(problem_id=None, solution=None):
    if not problem_id or solution:
        session = create_session()
        session_id = session.get('data').get('session_id')
        print(session_id)
        add_user_to_session(session_id)

        username = 'TestUser'
        problem = get_new_problem(session_id, username)
        problem_to_solve = problem.get('data').get('problem')
        problem_id = problem.get('data').get('question_id')
        solution = eval(problem_to_solve)

    params = json.dumps({
        'problem_id': problem_id,
        'answer': solution
    })
    r = requests.post(
        url=BASE_URL + '/api/session/{}/user/{}/solution'.format(
            session_id,
            username
        ), 
        data=params
    )
    print(r.status_code)
    assert r.status_code == 200
    # print(r.text)
    return r.json() if r.status_code == 200 else None

def test_api():
    submit_problem_solution(problem_id=None, solution=None)
    # session_id = session['']

if __name__ == "__main__":
    # submit_problem_solution()
    session = create_session()
    session_id = session.get('data').get('session_id')
    # print(session_id)
    add_user_to_session(session_id)

    username = 'TestUser'
    problem = get_new_problem(session_id, username)
    problem_to_solve = problem.get('data').get('problem')
    problem_id = problem.get('data').get('question_id')
    solution = eval(problem_to_solve)
    # print(problem)
    submit_problem_solution(problem_id, solution)