import unittest
from unittest.mock import Mock, patch
import json
from app import create_app

class TestDoublesDemonstration(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        
    # Example using a Stub
    def test_travel_endpoint_with_stub(self):
        """
        This test uses a stub to provide predetermined data,
        focusing on testing the endpoint's state handling
        """
        # Create a stub for DynamoDB response
        stub_destinations = [{
            "destination": "Test City, Test Country",
            "duration": "5hr 30m",
            "continent": "Europe",
            "best_season": "Summer"
        }]
        
        # Using a context manager to replace boto3.resource with our stub
        with patch('boto3.resource') as stub_dynamo:
            # Configure the stub to return our test data
            mock_table = Mock()
            mock_table.scan.return_value = {'Items': stub_destinations}
            stub_dynamo.return_value.Table.return_value = mock_table
            
            # Make request to the endpoint
            response = self.client.get('/travel?continent=Europe&max_duration=6')
            data = json.loads(response.data)
            
            # We only care about the response structure and data
            self.assertEqual(response.status_code, 200)
            self.assertIn('recommended_destination', data)
            self.assertIn('flight_duration', data)
            self.assertEqual(data['continent'], 'Europe')

    # Example using a Mock
    def test_meal_endpoint_with_mock(self):
        """
        This test uses a mock to verify interactions,
        focusing on testing the behavior and interactions
        """
        test_meal_id = "123"
        expected_meal = {
            'id': test_meal_id,
            'name': 'Test Meal',
            'description': 'Test Description'
        }
        
        # Create a mock for DynamoDB
        with patch('boto3.resource') as mock_dynamo:
            # Configure the mock
            mock_table = Mock()
            mock_table.get_item.return_value = {'Item': expected_meal}
            mock_dynamo.return_value.Table.return_value = mock_table
            
            # Make request to the endpoint
            response = self.client.get(f'/meal/{test_meal_id}')
            
            # Verify the interactions
            mock_dynamo.assert_called_once()
            mock_table.get_item.assert_called_once_with(
                Key={'id': test_meal_id}
            )
            
            # Also verify the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), expected_meal)

    def test_meal_endpoint_error_handling_with_mock(self):
        """
        This test uses a mock to verify error handling behavior
        """
        test_meal_id = "nonexistent"
        
        # Create a mock that simulates a DynamoDB error
        with patch('boto3.resource') as mock_dynamo:
            # Configure mock to raise an exception
            mock_table = Mock()
            mock_table.get_item.side_effect = Exception("DynamoDB error")
            mock_dynamo.return_value.Table.return_value = mock_table
            
            # Make request to the endpoint
            response = self.client.get(f'/meal/{test_meal_id}')
            
            # Verify error handling
            self.assertEqual(response.status_code, 500)
            data = json.loads(response.data)
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'Failed to access DynamoDB')

if __name__ == '__main__':
    unittest.main()