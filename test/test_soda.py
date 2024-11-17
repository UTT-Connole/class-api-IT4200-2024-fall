import pytest
from app import create_app
import json 

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_random_soda(client):
    """Test the soda endpoint returns a valid soda brand, size, and ice option"""
    response = client.get('/soda')
    assert response.status_code == 200  # Check if the status code is 200 (OK)
    
    json_data = response.get_json()
    assert 'soda' in json_data  # Check if 'soda' key is in the response
    assert 'size' in json_data  # Check if 'size' key is in the response
    assert 'ice' in json_data   # Check if 'ice' key is in the response

    # Check if the returned soda is one of the valid options
    valid_sodas = ['Fanta', 'Coca Cola', 'Sprite', 'Mountain Dew', 'Dr. Pepper']
    assert json_data['soda'] in valid_sodas, "Returned soda is not in the list of valid sodas"

    # Check if the returned size is one of the valid options
    valid_sizes = ['Personal', '2 Liter']
    assert json_data['size'] in valid_sizes, "Returned size is not in the list of valid sizes"

    # Check if the returned ice option is valid
    valid_ice_options = ['Ice', 'No Ice']
    assert json_data['ice'] in valid_ice_options, "Returned ice option is not in the list of valid ice options"

def test_get_all_sodas(client):
    """Test the soda endpoint returns all soda brands when queried with all=true"""
    response = client.get('/soda?all=true')
    assert response.status_code == 200  # Check if the status code is 200 (OK)

    json_data = response.get_json()
    assert 'sodas' in json_data  # Check if 'sodas' key is in the response

    # Check if the returned list matches the soda options
    expected_sodas = ['Fanta', 'Coca Cola', 'Sprite', 'Mountain Dew', 'Dr. Pepper']
    assert json_data['sodas'] == expected_sodas, "The returned sodas list doesn't match the expected list"
