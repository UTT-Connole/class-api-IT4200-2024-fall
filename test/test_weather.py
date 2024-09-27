import pytest
from app import create_app 

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
def test_weather_content_type(client):
    """Test if the weather endpoint returns a response in JSON format"""
    response = client.get('/weather/Paris')
    assert response.content_type == 'application/json'

def test_weather_error_response(client):
    """Test if the weather endpoint returns a 404 code when no city is given"""
    response = client.get('/weather')
    assert response.status_code == 404

    