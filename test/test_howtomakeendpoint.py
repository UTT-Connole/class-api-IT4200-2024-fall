import pytest
from app import create_app

def test_content_format(client):
    """Test to see if howToMakeEndpoint returns JSON format"""
    response = client.get("/howToMakeEndpoint")
    assert response.content_type == 'application/json'

def test_get_specific_step(client):
    """Test to retrieve a specific step using the 'step' query parameter"""
    response = client.get("/howToMakeEndpoint?step=2")
    assert response.status_code == 200
    assert response.json == {"step 2": "Create app"}

