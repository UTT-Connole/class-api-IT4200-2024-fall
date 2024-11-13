import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_get_items_invalid_min_price(client):
    """Test fetching items with an invalid minimum price (e.g., a string instead of an integer)."""
    response = client.get('/items/not_a_number')
    assert response.status_code == 404