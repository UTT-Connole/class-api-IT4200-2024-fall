import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

# Test for getting all quotes
def test_get_all_quotes(client):
    response = client.get('/quotes')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'author' in data[0]
    assert 'quote' in data[0]

# Test for getting a random quote
def test_get_random_quote(client):
    response = client.get('/quotes?random=true')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert 'author' in data
    assert 'quote' in data
