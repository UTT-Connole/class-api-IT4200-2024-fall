import pytest
from app import create_app

def test_content_format(client):
    """Test to see if howtomakeendpoint returns JSON format"""
    response = client.get("/howToMakeEndpoint")
    assert response.content_type == 'application/json'


