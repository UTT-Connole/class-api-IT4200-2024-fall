def test_tennis_fact(client):
    response = client.get('/tennis_fact')
    assert response.status_code == 200
    data = response.get_json()
    assert "fact" in data
    assert isinstance(data['fact'], str)