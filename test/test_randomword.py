import pytest
from app import create_app

def test_random_word_status_code(client):
    """Test if the randomWord endpoint returns a 200 status code"""
    response = client.get('/randomWord')
    assert response.status_code == 200

def test_random_word_content_type(client):
    """Test if the randomWord endpoint returns a response in JSON format"""
    response = client.get('/randomWord')
    assert response.content_type == 'application/json'

def test_random_word_contains_word(client):
    """Test if the randomWord endpoint returns a valid word in the JSON response"""
    response = client.get('/randomWord')
    json_data = response.get_json()
    assert 'word' in json_data
    assert isinstance(json_data['word'], str)
    assert len(json_data['word']) > 0  # Ensure the word is not empty