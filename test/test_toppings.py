import pytest
from app import create_app
import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_pizza_contains_valid_crust(client):
    """Test if the pizza contains a valid crust option."""
    response = client.get('/pizzaToppings')
    json_data = response.get_json()
    
    valid_crusts = ["Hand Tossed", "Handmade Pan", "Crunchy Thin Crust"]
    assert json_data['crust'] in valid_crusts  

def test_pizza_contains_three_toppings(client):
    """Test if the pizza contains exactly three toppings."""
    response = client.get('/pizzaToppings')
    json_data = response.get_json()
    
    assert len(json_data['toppings']) == 3 
    for topping in json_data['toppings']:
        assert 'topping' in topping 
