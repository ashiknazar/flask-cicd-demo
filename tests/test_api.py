import unittest
from app import create_app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_health_check(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "Healthy"})

    def test_multiply(self):
        response = self.client.post('/multiply')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['result'], 15)

if __name__ == '__main__':
    unittest.main()
