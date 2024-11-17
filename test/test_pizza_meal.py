import pytest
from app import create_app
import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test the pizza meal endpoint for valid crust options
def test_pizza_meal_contains_valid_crust(client):
    """Test if the pizza meal contains a valid crust option."""
    response = client.get('/pizza_meal')
    json_data = response.get_json()
    
    valid_crusts = ["Hand Tossed", "Handmade Pan", "Crunchy Thin Crust"]
    assert json_data['pizza']['crust'] in valid_crusts, "Crust is not one of the valid options"

# Test that the pizza meal contains exactly three toppings
def test_pizza_meal_contains_three_toppings(client):
    """Test if the pizza meal contains exactly three toppings."""
    response = client.get('/pizza_meal')
    json_data = response.get_json()
    
    assert len(json_data['pizza']['toppings']) == 3, "There should be exactly three toppings"
    for topping in json_data['pizza']['toppings']:
        assert isinstance(topping, dict), "Each topping should be a dictionary"
        assert 'topping' in topping, "Each dictionary should have a 'topping' key"

# Test the pizza meal sauce selection
def test_pizza_meal_sauce_selection(client):
    """Test if the pizza meal has a valid sauce."""
    response = client.get('/pizza_meal')
    json_data = response.get_json()
    
    valid_sauces = ["Tomato Sauce", "Alfredo Sauce", "Ranch Sauce"]
    assert json_data['pizza']['sauce'] in valid_sauces, "Sauce is not one of the valid options"

# Test for Cheese: Default cheese level
def test_pizza_meal_default_cheese(client):
    """Test if the default cheese level is Regular Cheese."""
    response = client.get('/pizza_meal')  # No cheese parameter provided
    json_data = response.get_json()
    
    assert json_data['pizza']['cheese'] == "Regular Cheese", "Default cheese level should be Regular Cheese"

# Test for Cheese: Custom valid cheese level
def test_pizza_meal_custom_cheese(client):
    """Test if a valid cheese level is accepted."""
    response = client.get('/pizza_meal?cheese=Extra Cheese')  # Custom cheese parameter
    json_data = response.get_json()
    
    assert json_data['pizza']['cheese'] == "Extra Cheese", "Cheese level should be Extra Cheese"

# Test for Cheese: Invalid cheese level
def test_pizza_meal_invalid_cheese(client):
    """Test if an invalid cheese level returns an error."""
    response = client.get('/pizza_meal?cheese=InvalidCheese')
    assert response.status_code == 400, "Invalid cheese level should return status code 400"

# Test: Half-and-Half Pizza Option
def test_pizza_meal_half_and_half_option(client):
    """Test if the half-and-half option returns two sets of toppings."""
    response = client.get('/pizza_meal?half_and_half=true')  # Request half-and-half pizza
    json_data = response.get_json()

    assert 'half1_toppings' in json_data['pizza'], "The first half toppings should be present in the response"
    assert 'half2_toppings' in json_data['pizza'], "The second half toppings should be present in the response"
    assert len(json_data['pizza']['half1_toppings']) == 3, "First half should have exactly three toppings"
    assert len(json_data['pizza']['half2_toppings']) == 3, "Second half should have exactly three toppings"

# Test: Special Type Pizza Option
def test_pizza_meal_special_type(client):
    """Test if the pizza meal has a valid special type."""
    response = client.get('/pizza_meal')
    json_data = response.get_json()

    valid_special_types = ["Regular", "Gluten-Free", "Vegan", "Keto"]
    assert 'special_type' in json_data['pizza'], "The 'special_type' key should be present in the response"
    assert json_data['pizza']['special_type'] in valid_special_types, "Special type should be one of the valid options"

# Test: Soda inclusion in the pizza meal
def test_pizza_meal_includes_soda(client):
    """Test if the pizza meal includes a soda with valid brand, size, and ice options."""
    response = client.get('/pizza_meal')
    json_data = response.get_json()

    valid_sodas = ['Fanta', 'Coca Cola', 'Sprite', 'Mountain Dew', 'Dr. Pepper']
    valid_sizes = ['Personal', '2 Liter']
    valid_ice_options = ['With Ice', 'No Ice']

    assert 'soda' in json_data, "Soda should be included in the meal response"
    assert json_data['soda']['brand'] in valid_sodas, "Soda brand should be one of the valid options"
    assert json_data['soda']['size'] in valid_sizes, "Soda size should be one of the valid options"
    assert json_data['soda']['ice'] in valid_ice_options, "Soda ice option should be one of the valid options"

# Test all sodas option within the meal
def test_pizza_meal_all_sodas(client):
    """Test if the 'all' query for soda within the pizza meal returns all soda brands."""
    response = client.get('/pizza_meal?soda=all')
    json_data = response.get_json()

    expected_sodas = ['Fanta', 'Coca Cola', 'Sprite', 'Mountain Dew', 'Dr. Pepper']
    assert 'sodas' in json_data['soda'], "The 'sodas' key should be present in the soda response"
    assert json_data['soda']['sodas'] == expected_sodas, "The returned sodas list doesn't match the expected list"
