import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calc_add(client):
    """Test the add operation"""
    response = client.get('/calc?x=10&y=5&op=add')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 15

def test_calc_subtract(client):
    """Test the subtract operation"""
    response = client.get('/calc?x=10&y=5&op=subtract')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 5

def test_calc_multiply(client):
    """Test the multiply operation"""
    response = client.get('/calc?x=10&y=5&op=multiply')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 50

def test_calc_divide(client):
    """Test the divide operation"""
    response = client.get('/calc?x=10&y=5&op=divide')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 2.0

def test_calc_divide_by_zero(client):
    """Test divide by zero"""
    response = client.get('/calc?x=10&y=0&op=divide')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == "You cannot divide by 0"

def test_calc_mod(client):
    """Test the mod operation"""
    response = client.get('/calc?x=10&y=5&op=mod')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 0

def test_calc_mod_by_zero(client):
    """Test mod by zero"""
    response = client.get('/calc?x=10&y=0&op=mod')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == "You cannot take modulus by 0"

def test_calc_square(client):
    """Test the square operation"""
    response = client.get('/calc?x=10&op=square')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 100

def test_calc_sqrt(client):
    """Test the square root operation"""
    response = client.get('/calc?x=16&op=sqrt')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 4.0

def test_calc_sqrt_negative(client):
    """Test the square root of a negative number"""
    response = client.get('/calc?x=-16&op=sqrt')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == "Cannot take square root of a negative number"

def test_calc_decimal_negative(client):
    """Test if a negative input for decimal returns an error."""
    response = client.get('/calc?x=-1&y=&op=decimal')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 'Not compatible with non-integer or negative input'

def test_decimal_float(client):
    """Test if a float input for decimal returns an error."""
    response = client.get('/calc?x=5.5&y=&op=decimal')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == 'Invalid Input. Must be a number.'

def test_binary_float(client):
    """Test if a float input for binary returns an error."""
    response = client.get('/calc?x=5.5&y=&op=binary')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == 'Invalid Input. Must be a number.'

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
    json_data = response.get_json()
    assert json_data['error'] == 'Missing input x'

def test_binary_blank(client):
    """Test if a blank input for binary returns an error."""
    response = client.get('/calc?x=&y=&op=binary')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == 'Missing input x'

def test_calc_power(client):
    """Test the power operation"""
    response = client.get('/calc?x=2&y=3&op=power')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 8

def test_calc_cube(client):
    """Test the cube operation"""
    response = client.get('/calc?x=3&op=cube')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 27

def test_calc_exp(client):
    """Test the exponential operation"""
    response = client.get('/calc?x=1&op=exp')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == math.exp(1)
