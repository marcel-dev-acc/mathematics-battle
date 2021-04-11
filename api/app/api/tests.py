from django.test import TestCase
from django.test import Client
import json
import requests

# Create your tests here.
class APITestCase(TestCase):
    def check_api_status(self):
        """Validate if API is responsive."""
        client = Client()
        response = client.get(path='/api/status')
        self.assertEqual(response.status_code, 200)

    def create_session(self):
        """Check that a session can be created."""
        client = Client()
        response = client.post(path='/api/create_session', data={})
        self.assertEqual(response.status_code, 200)

    def get_sessions(self):
        """Check that a list is returned."""
        client = Client()
        response = client.get(path='/api/sessions')
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            sessions = response.json().get('data')
            self.assertEqual(isinstance(sessions, list), True)

    def add_user_to_session(self):
        """Check that a user can be added to a session."""
        client = Client()
        response = client.post(path='/api/create_session', data={})
        # self.assertEqual(response.status_code, 200)
        if response.status_code != 200:
            self.assertEqual(True, False)
        session_id = response.json().get('data').get('session_id')
        response = client.put(
            path='api/session/{}/user'.format(session_id),
            data=json.dumps({
                'username': 'TestUser'
            })

        )
        self.assertEqual(response.status_code, 200)