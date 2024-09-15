import pytest, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_valid_color_red(client):
    response = client.get('/color?color=red')
    assert b'The hex code for red is #FF0000' in response.data

def test_invalid_color(client):
    response = client.get('/color?color=invalidcolor')
    assert b'Invalid color name' in response.data

def test_case_insensitive_red(client):
    response = client.get('/color?color=ReD')
    assert b'The hex code for ReD is #FF0000' in response.data

def test_empty_color(client):
    response = client.get('/color?color=')
    assert b'Invalid color name' in response.data

if __name__ == '__main__':
    pytest.main()