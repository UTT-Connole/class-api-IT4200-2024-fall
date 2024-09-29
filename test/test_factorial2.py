import pytest
from app import app  # Ensure the correct import for your Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_factorial(client):
    # Test a successful factorial calculation
    response = client.get('/factorial?number=5')
    assert response.status_code == 200
    assert response.json == {'result': 120}

    # Test edge case: factorial of 0
    response = client.get('/factorial?number=0')
    assert response.status_code == 200
    assert response.json == {'result': 1}

    # Test invalid input
    response = client.get('/factorial?number=-1')
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid input'}

    # Test non-integer input
    response = client.get('/factorial?number=abc')
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid input'}
