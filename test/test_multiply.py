import unittest
from app import app

class MultiplyTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_multiply_valid_input(self):
        # Test with valid inputs
        response = self.app.get('/multiply?a=5&b=10')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 50.0)

    def test_multiply_invalid_input(self):
        # Test with invalid input (non-numeric)
        response = self.app.get('/multiply?a=5&b=abc')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid input')

    def test_multiply_missing_input(self):
        # Test with missing input (no parameter b)
        response = self.app.get('/multiply?a=5')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid input')

    def test_multiply_no_input(self):
        # Test with no input parameters
        response = self.app.get('/multiply')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid input')

if __name__ == '__main__':
    unittest.main()
