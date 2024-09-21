import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_pizza_toppings_status_code(client):
    """Test if the /pizzaToppings endpoint returns a 200 status code"""
    response = client.get('/pizzaToppings')
    assert response.status_code == 200

def test_pizza_toppings_response_structure(client):
    """Test if the /pizzaToppings endpoint returns a valid JSON structure"""
    response = client.get('/pizzaToppings')
    json_data = response.get_json()
    
    assert 'sauce' in json_data
    assert 'toppings' in json_data
    assert isinstance(json_data['sauce'], str) 
    assert isinstance(json_data['toppings'], list)  
    assert len(json_data['toppings']) == 3 

