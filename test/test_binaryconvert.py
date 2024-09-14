#import pytest
#from app import create_app

def test_status_code(client):
    response = client.get('/convertToBinary')
    assert response.status_code == 200
    