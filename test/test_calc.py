import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

#Tests add operator
def test_calc_add(client):
    """Test the add operation"""
    response = client.get('/calc?x=10&y=5&op=add')
    assert response.data.decode() == '15'

#Tests subtract operator
def test_calc_subtract(client):
    """Test the subtract operation"""
    response = client.get('/calc?x=10&y=5&op=subtract')
    assert response.data.decode() == '5'

#Tests multiply operator
def test_calc_multiply(client):
    """Test the multiply operation"""
    response = client.get('/calc?x=10&y=5&op=multiply')
    assert response.data.decode() == '50'
    
#Tests divide
def test_calc_divide(client):
    """Test the divide operation"""
    response = client.get('/calc?x=10&y=5&op=divide')
    assert response.data.decode() == '2.0'
    
#Tests divide by 0
def test_calc_divide_by_zero(client):
    """Test divide by zero"""
    response = client.get('/calc?x=10&y=0&op=divide')
    assert response.data.decode() == 'You cannot divide by 0'
    
#Tests if not a valid operator
def test_calc_invalid_operator(client):
    """Test invalid operator"""
    response = client.get('/calc?x=10&y=5&op=wrong')
    assert response.data.decode() == 'You might have spelled something wrong or there is not the option. The current options are: add, subtract, multiply, divide'