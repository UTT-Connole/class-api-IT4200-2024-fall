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
    assert json_data['crust'] in valid_crusts, "Crust is not one of the valid options"

def test_pizza_contains_three_toppings(client):
    """Test if the pizza contains exactly three toppings."""
    response = client.get('/pizzaToppings')
    json_data = response.get_json()
    print(json_data)  # This line can eventually be removed once issues are resolved
    
    assert len(json_data['toppings']) == 3, "There should be exactly three toppings"
    for topping in json_data['toppings']:
        assert isinstance(topping, str), "Each topping should be a string"

def test_pizza_sauce_selection(client):
    """Test if the pizza has a valid sauce."""
    response = client.get('/pizzaToppings')
    json_data = response.get_json()
    
    valid_sauces = ["Tomato Sauce", "Alfredo Sauce", "Ranch Sauce"]
    assert json_data['sauce'] in valid_sauces, "Sauce is not one of the valid options"
