from flask import jsonify
import pytest
import random
from app import app

# Using Flask test client to simulate requests to the `travel` endpoint
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_travel_default_response(client):
    """Test if the travel endpoint returns a default response without filters."""
    response = client.get('/travel')
    data = response.get_json()
    
    assert response.status_code == 200
    assert "recommended_destination" in data
    assert "flight_duration" in data

def test_travel_with_max_duration(client):
    """Test if the travel endpoint filters based on max_duration."""
    response = client.get('/travel?max_duration=4')
    data = response.get_json()

    assert response.status_code == 200
    assert "recommended_destination" in data
    assert "flight_duration" in data

