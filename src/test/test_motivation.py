import pytest
import random
from flask import jsonify

# Test: Verify the content type is JSON
def test_motivation_content_type(client):
    """Test if the motivation endpoint returns a response in JSON format"""
    response = client.get('/motivation')
    assert response.content_type == 'application/json'

# Test: Check if a motivational quote is present in the response
def test_motivation_contains_quote(client):
    """Test if the motivation endpoint returns a valid motivational quote in the JSON response"""
    response = client.get('/motivation')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'motivational_quote' in json_data
    assert isinstance(json_data['motivational_quote'], str)
    assert len(json_data['motivational_quote']) > 0  # Ensure the quote is not an empty string

# Test: Multiple requests return quotes from the predefined list
def test_motivation_multiple_requests(client):
    """Test if multiple requests to the motivation endpoint return different quotes from the list"""
    quotes_set = set()
    predefined_quotes = [
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Believe you can and you're halfway there.",
        "Act as if what you do makes a difference. It does.",
        "The harder you work for something, the greater you’ll feel when you achieve it."
    ]
    
    for _ in range(10):  # Make 10 requests to the endpoint
        response = client.get('/motivation')
        json_data = response.get_json()
        quote = json_data['motivational_quote']
        quotes_set.add(quote)
        assert quote in predefined_quotes  # Verify the returned quote is from the list
    
    # Ensure that at least more than 1 unique quote was returned in 10 requests
    assert len(quotes_set) > 1, "The same quote was returned for all requests."

# Test: Check for invalid response status
def test_motivation_status_code(client):
    """Test if the motivation endpoint returns a 200 OK status"""
    response = client.get('/motivation')
    assert response.status_code == 200
