import pytest

def test_generate_name(client):
    """Test the '/generateName' endpoint"""
    response = client.get('/generateName')
    assert response.status_code == 200
    data = response.get_json()

    assert "name" in data
    assert isinstance(data['name'], str)
    assert data['name'] in ["Eve", "Jack", "Liam", "Mia"]