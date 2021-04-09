from django.test import TestCase
from django.test import Client

# Create your tests here.
class APITestCase(TestCase):
    def check_api_status(self):
        """Validate if API is responsive."""
        client = Client()
        response = client.get('/api/status')
        self.assertEqual(response.status_code, 200)