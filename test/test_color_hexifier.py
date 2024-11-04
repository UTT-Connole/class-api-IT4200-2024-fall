import pytest, sys, os
from flask import url_for

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_color_hexifier_page_load(client):
    """Test if the color hexifier HTML page loads successfully"""
    response = client.get('/color')
    assert response.status_code == 200
    assert b"Color Hexifier" in response.data

def test_valid_color_red(client):
    """Test the color hex retrieval for a valid color"""
    response = client.get('/get_color_hex?color=red')
    data = response.get_json()
    assert response.status_code == 200
    assert data['hex_code'] == '#FF0000'

def test_invalid_color(client):
    """Test the color hex retrieval with an invalid color"""
    response = client.get('/get_color_hex?color=invalidcolor')
    data = response.get_json()
    assert response.status_code == 400
    assert data['error'] == "Invalid color name"

def test_case_insensitive_red(client):
    """Test if color hex retrieval is case insensitive"""
    response = client.get('/get_color_hex?color=ReD')
    data = response.get_json()
    assert response.status_code == 200
    assert data['hex_code'] == '#FF0000'

def test_empty_color(client):
    """Test the color hex retrieval with an empty color input"""
    response = client.get('/get_color_hex?color=')
    data = response.get_json()
    assert response.status_code == 400
    assert data['error'] == "Invalid color name"

if __name__ == '__main__':
    pytest.main()