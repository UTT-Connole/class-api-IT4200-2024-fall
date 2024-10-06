import pytest
from app import create_app

import json

def test_get_favorite_quote():
    app = create_app()
    client = app.test_client()

    # Test the GET request for the original quote
    response = client.get('/favoritequote')
    assert response.status_code == 200
    assert response.json == {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs"
    }

def test_post_favorite_quote():
    app = create_app()
    client = app.test_client()

    # Test the POST request to add a new quote
    new_quote = {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"}
    response = client.post('/favoritequote', data=json.dumps(new_quote), content_type='application/json')
    assert response.status_code == 201
    assert response.json == {"message": "New favorite quote added!", "quote": new_quote}
