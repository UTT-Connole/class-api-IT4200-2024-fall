import pytest, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_fortune_status_code(client):
    """Test if the fortune endpoint returns a 200 status code"""
    response = client.get('/fortune')
    assert response.status_code == 200

def test_fortune_structure(client):
    """Test if the response structure is a JSON object with 'fortune' key"""
    response = client.get('/fortune')
    json_data = response.get_json()
    assert 'fortune' in json_data

def test_fortune_content(client):
    """Test if the fortune returned is from the predefined list"""
    valid_fortunes = [
        "You will find a fortune.",
        "A fresh start will put you on your way.",
        "Fortune favors the brave.",
        "Good news will come to you by mail."
    ]
    response = client.get('/fortune')
    json_data = response.get_json()
    assert json_data['fortune'] in valid_fortunes

def test_fortune_not_empty(client):
    """Test if the returned fortune is not an empty string"""
    response = client.get('/fortune')
    json_data = response.get_json()
    assert json_data['fortune'] != ''