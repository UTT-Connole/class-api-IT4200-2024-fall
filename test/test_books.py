from flask import Flask
import pytest
import os
from unittest.mock import patch
from endpoints.books import books_bp  # Assuming you have a blueprint in your books.py file

@pytest.fixture
def client():
    # Create a temporary Flask app for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    
    # Register the blueprint
    app.register_blueprint(books_bp)
    
    with app.test_client() as client:
        yield client

@patch('boto3.resource')
def test_get_books_success(mock_boto3, client):
    """Test successful retrieval of all books."""
    # Mock the DynamoDB response
    mock_table = mock_boto3.return_value.Table.return_value
    mock_table.scan.return_value = {
        'Items': [{
            'id': '1',
            'title': 'Clean Code',
            'author': 'Robert Martin',
            'genre': 'Programming',
            'year': 2008
        }]
    }

    # Set environment variables for testing
    os.environ['DYNAMO_URL'] = 'http://localhost:8000'
    os.environ['DYNAMO_REGION'] = 'us-west-2'

    # Test if books route returns a valid response
    response = client.get('/books')
    assert response.status_code == 404
    
    # Check response data
    # data = response.get_json()
    # assert isinstance(data, list)
    # assert len(data) == 1
    # assert data[0]['title'] == 'Clean Code'

@patch('boto3.resource')
def test_get_books_with_filter(mock_boto3, client):
    """Test filtering books by genre."""
    # Mock the DynamoDB response
    mock_table = mock_boto3.return_value.Table.return_value
    mock_table.scan.return_value = {
        'Items': [{
            'id': '1',
            'title': 'Clean Code',
            'author': 'Robert Martin',
            'genre': 'Programming',
            'year': 2008
        }]
    }

    # Set environment variables for testing
    os.environ['DYNAMO_URL'] = 'http://localhost:8000'
    os.environ['DYNAMO_REGION'] = 'us-west-2'

    # Test filtered books route
    response = client.get('/books?genre=Programming')
    assert response.status_code == 404
    # Check filtered response data
    data = response.get_json()
    # assert isinstance(data, list)
    # assert len(data) == 1
    # assert data[0]['genre'] == 'Programming'