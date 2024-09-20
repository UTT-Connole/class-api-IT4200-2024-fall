import pytest, app

def test_status(client):
    response = client.get('/fortune')
    assert response.status_code == 200