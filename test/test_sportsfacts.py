def test_sports_fact(client):
    response = client.get('/sports_fact')
    assert response.status_code == 200
    data = response.get_json()
    assert "fact" in data
    assert isinstance(data['fact'], str)