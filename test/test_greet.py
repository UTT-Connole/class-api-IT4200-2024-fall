def test_greet(client):
    """Test the '/greet' endpoint"""
    response = client.get('/greet')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Welcome to the API!"}

def test_greet_with_name(client):
    """Test the '/greet/<name>' endpoint"""
    response = client.get('/greet/John')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, John!"}
