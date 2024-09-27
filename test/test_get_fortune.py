def test_fortune(client):
    response = client.get('/fortune')
    assert response.status_code == 200
    assert b'You will have a great day!' in response.data