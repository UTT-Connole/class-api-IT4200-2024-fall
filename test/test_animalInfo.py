import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_valid_animal(client):
    response = client.get('/animalInfo?animal=dog')
    assert response.status_code == 200
    data = response.get_json()  # Get the JSON response as a Python dictionary
    assert data["type"] == "mammal"
    assert data["sound"] == "bark"

def test_invalid_animal(client):
    response = client.get('/animalInfo?animal=unicorn')
    assert response.status_code == 404
    assert b'Animal not found' in response.data

def test_case_insensitive_animal(client):
    response = client.get('/animalInfo?animal=CaT')
    assert response.status_code == 200
    data = response.get_json()  # Get the JSON response as a Python dictionary
    assert data["type"] == "mammal"
    assert data["sound"] == "meow"

def test_no_animal_provided(client):
    response = client.get('/animalInfo')
    assert response.status_code == 404
    assert b'Animal not found' in response.data
