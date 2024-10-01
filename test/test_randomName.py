def test_random_name(client):
    response = client.get('/randomName')
    assert response.status_code == 200
    data = response.get_json()
    assert "name" in data 
    assert isinstance(data['name'], str) 
    assert data['name'] in ["Alice", "Bob", "Charlie", "Diana"]
