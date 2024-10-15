def test_greet_without_name(client):
    response = client.get('/greet')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Hello, Welcome to the API!"

def test_greet_with_name(client):
    response = client.get('/greet?name=Alice')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Hello, Alice!"
