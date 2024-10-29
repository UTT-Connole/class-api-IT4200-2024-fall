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

def test_patch_favorite_quote_success(client):
    # Test the PATCH request to update an existing favorite quote
    updated_data = {
        "author": "Steve Jobs",
        "quote": "Innovation distinguishes between a leader and a follower."
    }
    response = client.patch('/favoritequote', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 200
    assert response.json == {
        "message": "Favorite quote updated!",
        "quote": {
            "quote": "Innovation distinguishes between a leader and a follower.",
            "author": "Steve Jobs"
        }
    }

def test_patch_non_existent_quote(client):
    # Test the PATCH request to update a non-existent favorite quote
    updated_data = {
        "author": "Non Existent Author",
        "quote": "This quote does not exist."
    }
    response = client.patch('/favoritequote', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 404
    assert response.json == {"error": "Quote not found for the given author."}

def test_patch_quote_invalid_data(client):
    # Test the PATCH request with missing author
    updated_data = {
        "quote": "This should not work."
    }
    response = client.patch('/favoritequote', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 404  # Assuming 404 for invalid data
    assert response.json == {"error": "Quote not found for the given author."}