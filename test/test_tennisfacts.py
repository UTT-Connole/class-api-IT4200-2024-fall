import pytest
from app import create_app

def test_tennis_facts_status_code(client):
    response = client.get('/tennisFacts')
    assert response.status_code == 200

def test_tennis_facts_content_type(client):
    response = client.get('/tennisFacts')
    assert response.content_type == 'application/json'

def test_tennis_facts_contains_facts(client):
    response = client.get('/tennisFacts')
    json_data = response.get_json()
    assert isinstance(json_data, list)
    assert len(json_data) > 0
    assert 'fact' in json_data[0]
    assert isinstance(json_data[0]['fact'], str)