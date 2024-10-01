import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Tests add operator
def test_calc_add(client):
    """Test the add operation"""
    response = client.get('/calc?x=10&y=5&op=add')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '15' in html_data

# Tests subtract operator
def test_calc_subtract(client):
    """Test the subtract operation"""
    response = client.get('/calc?x=10&y=5&op=subtract')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '5' in html_data

# Tests multiply operator
def test_calc_multiply(client):
    """Test the multiply operation"""
    response = client.get('/calc?x=10&y=5&op=multiply')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '50' in html_data
    
# Tests divide
def test_calc_divide(client):
    """Test the divide operation"""
    response = client.get('/calc?x=10&y=5&op=divide')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '2.0' in html_data
    
# Tests divide by 0
def test_calc_divide_by_zero(client):
    """Test divide by zero"""
    response = client.get('/calc?x=10&y=0&op=divide')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert 'You cannot divide by 0' in html_data
    
# Tests if not a valid operator
def test_calc_invalid_operator(client):
    """Test invalid operator"""
    response = client.get('/calc?x=10&y=5&op=wrong')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    operators_response = client.get('/calcop')
    available_operations = ', '.join(operators_response.get_json())
    expected_message = f"You might have spelled something wrong or there is not the option. The current options are: {available_operations}"
    assert expected_message in html_data

# Tests mod operator
def test_calc_mod(client):
    """Test the mod operation"""
    response = client.get('/calc?x=10&y=3&op=mod')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '1' in html_data

# Tests mod by 0
def test_calc_mod_by_zero(client):
    """Test mod by zero"""
    response = client.get('/calc?x=10&y=0&op=mod')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert 'You cannot take modulus by 0' in html_data

# Tests square operator
def test_calc_square(client):
    """Test the square operation"""
    response = client.get('/calc?x=4&op=square')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '16' in html_data

# Tests square root operator
def test_calc_sqrt(client):
    """Test the square root operation"""
    response = client.get('/calc?x=16&op=sqrt')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '4.0' in html_data

# Tests square root of a negative number
def test_calc_sqrt_negative(client):
    """Test the square root of a negative number"""
    response = client.get('/calc?x=-16&op=sqrt')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert 'Cannot take square root of a negative number' in html_data