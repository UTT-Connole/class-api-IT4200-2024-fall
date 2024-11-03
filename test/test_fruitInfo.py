import pytest
import json
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_non_existing_fruit(client):
    response = client.get('/fruitInfo?fruit=kiwi')
    data = json.loads(response.data)
    assert 'error' in data
    assert 'Available fruits' in data['error']

def test_post_new_fruit(client):
    response = client.post('/fruitInfo?fruit=plum&color=purple&taste=sweet')
    data = json.loads(response.data)
    assert 'message' in data
    assert data['message'] == 'plum added successfully!'

def test_post_fruit_missing_data(client):
    response = client.post('/fruitInfo?fruit=&color=yellow&taste=sour')
    data = json.loads(response.data)
    assert 'error' in data

def test_post_fruit_incomplete_data(client):
    response = client.post('/fruitInfo?fruit=cherry&color=red')
    data = json.loads(response.data)
    assert 'error' in data
    
def test_get_existing_fruit(client):
    response = client.get('/fruitInfo?fruit=peach')
    data = json.loads(response.data)
    assert 'fruit' in data
    assert data['fruit'] == 'peach'
    assert data['color'] == 'yellow'
    assert data['taste'] == 'sweet'

def test_get_all_fruits(client):
    response = client.get('/fruitInfo')
    data = json.loads(response.data)
    assert data
    assert 'plum' in data