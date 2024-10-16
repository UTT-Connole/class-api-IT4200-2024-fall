import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_version_endpoint(client):
    response = client.get('/version')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    json_data = response.get_json()
    assert 'version' in json_data

def test_current_version_endpoint(client):
    response = client.get('/current-version')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    json_data = response.get_json()
    assert 'version' in json_data