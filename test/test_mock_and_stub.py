
import unittest
from unittest.mock import Mock, patch
import json
import random
from app import create_app

class TestFlaskAPIEndpoints(unittest.TestCase):
    def setUp(self):
    
        self.app = create_app()
        self.client = self.app.test_client()


    def test_continents_endpoint_comprehensive(self):
    
        # Full continents retrieval test
        response = self.client.get('/continents')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        
        # Validate total number of continents
        expected_continents = 7  # Matches original implementation
        self.assertEqual(len(data), expected_continents, 
                         f"Expected {expected_continents} continents")
        
        # Validate continent structure
        required_keys = ['id', 'name', 'area', 'population']
        for continent in data:
            for key in required_keys:
                self.assertIn(key, continent, 
                              f"Continent missing {key} attribute")
            
            # Additional validation for specific attributes
            self.assertIsInstance(continent['id'], int, "ID must be an integer")
            self.assertIsInstance(continent['name'], str, "Name must be a string")
            self.assertIsInstance(continent['area'], int, "Area must be an integer")
            self.assertIsInstance(continent['population'], int, "Population must be an integer")


    def test_multiply_endpoint_precision(self):
    
        # Test basic integer multiplication
        response = self.client.get('/multiply?numbers=2,3,4')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(data['result'], 24, places=7)
        self.assertEqual(data['numbers_multiplied'], 3)

        # Test floating-point multiplication
        response = self.client.get('/multiply?numbers=1.5,2.5,3')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(data['result'], 11.25, places=7)

    def test_greet_endpoint(self):
       
        # Test default greeting
        response = self.client.get('/greet')
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Hello, Welcome to the API!')

        # Test personalized greeting
        response = self.client.get('/greet?name=Alice')
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Hello, Alice!')



if __name__ == '__main__':
    unittest.main()