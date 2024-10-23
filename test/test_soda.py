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
    """Test the soda endpoint returns a valid soda brand"""
    response = client.get('/soda')
    assert response.status_code == 200  # Check if the status code is 200 (OK)
    
    json_data = response.get_json()
    assert 'soda' in json_data  # Check if 'soda' key is in the response

    # Check if the returned soda is one of the valid options
    valid_sodas = ['Fanta', 'Coca Cola', 'Sprite', 'Mountain Dew', 'Dr. Pepper']
    assert json_data['soda'] in valid_sodas, "Returned soda is not in the list of valid sodas"

