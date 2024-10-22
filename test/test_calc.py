import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Updated tests

def test_decimal_negative(client):
    """Test if a negative input for decimal returns an error."""
    response = client.get('/calc?x=-1&y=&op=decimal')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 'Not compatible with non-integer or negative input'

def test_decimal_float(client):
    """Test if a float input for decimal returns an error."""
    response = client.get('/calc?x=5.5&y=&op=decimal')
    assert response.status_code == 400

def test_binary_float(client):
    """Test if a float input for binary returns an error."""
    response = client.get('/calc?x=5.5&y=&op=binary')
    assert response.status_code == 400

def test_decimal_str(client):
    """Test if a string input for decimal returns an error."""
    response = client.get('/calc?x=abc&y=&op=decimal')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == 'Invalid Input. Must be a number.'

def test_binary_str(client):
    """Test if a string input for binary returns an error."""
    response = client.get('/calc?x=abc&y=&op=binary')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == 'Invalid Input. Must be a number.'

def test_decimal_blank(client):
    """Test if a blank input for decimal returns an error."""
    response = client.get('/calc?x=&y=&op=decimal')
    assert response.status_code == 400

def test_binary_blank(client):
    """Test if a blank input for binary returns an error."""
    response = client.get('/calc?x=&y=&op=binary')
    assert response.status_code == 400
