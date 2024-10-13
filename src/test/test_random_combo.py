def test_two_mana_combo_no_color(client):
    """Test the '/twoManaCombos' endpoint without a color parameter"""
    response = client.get('/twoManaCombos')
    assert response.status_code == 200
    json_data = response.get_json()
    
    # Check if the response contains the expected keys
    assert "name" in json_data
    assert "color_1" in json_data
    assert "color_2" in json_data

    # List of possible two-mana combinations
    expected_combos = ["Azorius", "Boros", "Dimir", "Golgari", "Gruul", "Izzet", 
                       "Orzhov", "Rakdos", "Selesnya", "Simic"]
    
    # Ensure the random response name is one of the valid combinations
    assert json_data['name'] in expected_combos


def test_two_mana_combo_with_valid_color(client):
    """Test the '/twoManaCombos' endpoint with a valid color parameter"""
    response = client.get('/twoManaCombos?color=red')
    assert response.status_code == 200
    json_data = response.get_json()
    
    # Check if the response contains the expected keys
    assert "name" in json_data
    assert "color_1" in json_data
    assert "color_2" in json_data
    
    # The combo should have 'red' as one of the colors
    assert 'red' in [json_data['color_1'].lower(), json_data['color_2'].lower()]


def test_two_mana_combo_with_invalid_color(client):
    """Test the '/twoManaCombos' endpoint with an invalid color parameter"""
    response = client.get('/twoManaCombos?color=purple')
    assert response.status_code == 404
    json_data = response.get_json()
    
    # Check that an error message is returned
    assert "error" in json_data
    assert json_data["error"] == "No combinations found for the given color"