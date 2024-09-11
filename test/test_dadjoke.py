import pytest
from app import create_app 

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dadjoke_status_code(client):
    """Test if the dadjoke endpoint returns a 200 status code"""
    response = client.get('/dadjoke')
    assert response.status_code == 200

def test_dadjoke_content_type(client):
    """Test if the dadjoke endpoint returns a response in JSON format"""
    response = client.get('/dadjoke')
    assert response.content_type == 'application/json'

def test_dadjoke_contains_joke(client):
    """Test if the dadjoke endpoint returns a valid joke in the JSON response"""
    response = client.get('/dadjoke')
    json_data = response.get_json()
    assert 'joke' in json_data
    assert isinstance(json_data['joke'], str)
    assert len(json_data['joke']) > 0  # Ensure the joke is not an empty string

