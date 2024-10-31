import unittest
from app import app 

class ContinentApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_continents(self):
        """Test retrieving all continents"""
        response = self.app.get('/continents')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json, list))
        self.assertEqual(len(response.json), 7)

    def test_get_single_continent(self):
        """Test retrieving a single continent by ID"""
        response = self.app.get('/continents/3')  # Asia
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Asia')
        self.assertEqual(response.json['area'], 44579000)
        self.assertEqual(response.json['population'], 4641054775)

    def test_get_single_continent_not_found(self):
        """Test retrieving a non-existent continent by ID"""
        response = self.app.get('/continents/99')  # ID not in sample data
        self.assertEqual(response.status_code, 404)  # Check if the status code is 404
        self.assertIn("Continent not found", str(response.data))  # Ensure the error message is in the response
