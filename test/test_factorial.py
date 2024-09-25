
def test_zero(client):
    response = client.get('/factorial')
    assert response.status_code == 200
