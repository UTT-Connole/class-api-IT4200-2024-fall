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