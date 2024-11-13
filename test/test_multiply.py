from app import create_app
import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_multiply_valid_numbers(client):
    """Test multiplication with valid numbers."""
    response = client.get('/multiply?numbers=2,3,4')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 24.0
    assert json_data['numbers_multiplied'] == 3

def test_multiply_with_decimals(client):
    """Test multiplication with decimal numbers to handle precision."""
    response = client.get('/multiply?numbers=3.3,3.3,3.3')
    json_data = response.get_json()
    assert response.status_code == 200
    assert round(json_data['result'], 2) == 35.94  # Expected result 35.937
    assert json_data['numbers_multiplied'] == 3

def test_multiply_missing_numbers(client):
    """Test multiplication with no numbers provided in query."""
    response = client.get('/multiply')
    json_data = response.get_json()
    assert response.status_code == 400
    assert 'error' in json_data
    assert json_data['error'] == 'Please provide numbers to multiply'

def test_multiply_invalid_input(client):
    """Test multiplication with invalid (non-numeric) input."""
    response = client.get('/multiply?numbers=5,abc')
    json_data = response.get_json()
    assert response.status_code == 400
    assert 'error' in json_data
    assert json_data['error'] == 'Invalid input. Please provide valid numbers separated by commas'
