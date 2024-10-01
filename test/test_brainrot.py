import pytest
from app import create_app


def test_random_word_status_code(client):
    """Test if the brainrot endpoint returns a 200 status code"""
    response = client.get('/brainrot')
    assert response.status_code == 200

def test_brainrot_content_type(client):
    """Test if the brainrot endpoint returns a response in HTML format"""
    response = client.get('/brainrot')
    assert response.content_type == 'text/html; charset=utf-8'

def test_brainrot_contains_word(client):
    """Test if the brainrot endpoint returns a valid word in the HTML response"""
    response = client.get('/brainrot')
    assert response.status_code == 200  # Ensure the request was successful
    assert b'Injecting Brainrot Vocab:' in response.data  # Check if the phrase is in the HTML
    assert b'<strong>' in response.data  # Ensure there is a strong tag for the word

    # Optionally, you can extract the word from the HTML and verify its type
    # This requires using a regex or similar approach to parse the HTML
    
    # Here’s a simple way to extract the word using string methods
    start = response.data.find(b'<strong>') + len(b'<strong>')
    end = response.data.find(b'</strong>', start)
    brainrot_word = response.data[start:end].decode('utf-8')
    
    assert isinstance(brainrot_word, str)
    assert len(brainrot_word) > 0  # Ensure the word is not empty

def test_brainrot_word_uniqueness(client):
    """Test if multiple requests to the brainrot endpoint return different words"""
    words = set()
    for _ in range(10):  # Make 10 requests to the endpoint
        response = client.get('/brainrot')
        assert response.status_code == 200  # Ensure the request was successful
        
        start = response.data.find(b'<strong>') + len(b'<strong>')
        end = response.data.find(b'</strong>', start)
        brainrot_word = response.data[start:end].decode('utf-8')
        words.add(brainrot_word)  # Add the word to the set
    
    # There should be more than 1 unique word in 10 requests
    assert len(words) > 1, "The same word was returned for all requests."

def test_brainrot_word_length(client):
    """Test if the word returned from the brainrot endpoint is of reasonable length"""
    response = client.get('/brainrot')
    assert response.status_code == 200  # Ensure the request was successful

    start = response.data.find(b'<strong>') + len(b'<strong>')
    end = response.data.find(b'</strong>', start)
    word = response.data[start:end].decode('utf-8')
    
    # Ensure the word length is between 3 and 20 characters (as an example)
    assert 3 <= len(word) <= 20, f"The word '{word}' is of an unexpected length."
