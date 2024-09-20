import pytest
from app import create_app


def test_random_word_status_code(client):
    """Test if the brainrot endpoint returns a 200 status code"""
    response = client.get('/brainrot')
    assert response.status_code == 200

def test_random_word_content_type(client):
    """Test if the brainrot endpoint returns a response in JSON format"""
    response = client.get('/brainrot')
    assert response.content_type == 'application/json'

def test_random_word_contains_word(client):
    """Test if the brainrot endpoint returns a valid word in the JSON response"""
    response = client.get('/brainrot')
    json_data = response.get_json()
    assert 'word' in json_data
    assert isinstance(json_data['word'], str)
    assert len(json_data['word']) > 0  # Ensure the word is not empty

def test_brainrot_word_uniqueness(client):
    """Test if multiple requests to the brainrot endpoint return different words"""
    words = set()
    for _ in range(10):  # Make 10 requests to the endpoint
        response = client.get('/brainrot')
        json_data = response.get_json()
        words.add(json_data['word'])  # Add the word to the set
    
    # There should be more than 1 unique word in 10 requests
    assert len(words) > 1, "The same word was returned for all requests."

def test_brainrot_word_length(client):
    """Test if the word returned from the brainrot endpoint is of reasonable length"""
    response = client.get('/brainrot')
    json_data = response.get_json()
    word = json_data['word']
    
    # Ensure the word length is between 3 and 20 characters (as an example)
    assert 3 <= len(word) <= 20, f"The word '{word}' is of an unexpected length."
