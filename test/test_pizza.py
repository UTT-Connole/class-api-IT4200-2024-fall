
import pytest
from app import create_app
import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test the pizza endpoint for valid crust options
def test_pizza_contains_valid_crust(client):
    """Test if the pizza contains a valid crust option."""
    response = client.get('/pizza')
    json_data = response.get_json()
    
    valid_crusts = ["Hand Tossed", "Handmade Pan", "Crunchy Thin Crust"]
    assert json_data['crust'] in valid_crusts, "Crust is not one of the valid options"

# Test that the pizza contains exactly three toppings
def test_pizza_contains_three_toppings(client):
    """Test if the pizza contains exactly three toppings."""
    response = client.get('/pizza')
    json_data = response.get_json()
    
    assert len(json_data['toppings']) == 3, "There should be exactly three toppings"
    for topping in json_data['toppings']:
        assert isinstance(topping, dict), "Each topping should be a dictionary"
        assert 'topping' in topping, "Each dictionary should have a 'topping' key"

# Test the pizza sauce selection
def test_pizza_sauce_selection(client):
    """Test if the pizza has a valid sauce."""
    response = client.get('/pizza')
    json_data = response.get_json()
    
    valid_sauces = ["Tomato Sauce", "Alfredo Sauce", "Ranch Sauce"]
    assert json_data['sauce'] in valid_sauces, "Sauce is not one of the valid options"

# New Test for Cheese: Default cheese level
def test_pizza_default_cheese(client):
    """Test if the default cheese level is Regular Cheese."""
    response = client.get('/pizza')  # No cheese parameter provided
    json_data = response.get_json()
    
    assert json_data['cheese'] == "Regular Cheese", "Default cheese level should be Regular Cheese"

# New Test for Cheese: Custom valid cheese level
def test_pizza_custom_cheese(client):
    """Test if a valid cheese level is accepted."""
    response = client.get('/pizza?cheese=Extra Cheese')  # Custom cheese parameter
    json_data = response.get_json()
    
    assert json_data['cheese'] == "Extra Cheese", "Cheese level should be Extra Cheese"

# New Test for Cheese: Invalid cheese level
def test_pizza_invalid_cheese(client):
    """Test if an invalid cheese level returns an error."""
    response = client.get('/pizza?cheese=InvalidCheese')
    assert response.status_code == 400, "Invalid cheese level should return status code 400"

# New Test: Half-and-Half Pizza Option
def test_half_and_half_option(client):
    """Test if the half-and-half option returns two sets of toppings."""
    response = client.get('/pizza?half_and_half=true')  # Request half-and-half pizza
    json_data = response.get_json()

    assert 'half1_toppings' in json_data, "The first half toppings should be present in the response"
    assert 'half2_toppings' in json_data, "The second half toppings should be present in the response"
    assert len(json_data['half1_toppings']) == 3, "First half should have exactly three toppings"
    assert len(json_data['half2_toppings']) == 3, "Second half should have exactly three toppings"






