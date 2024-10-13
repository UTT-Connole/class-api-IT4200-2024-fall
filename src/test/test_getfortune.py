
def test_fortune_status_code(client):
    """Test if the fortune endpoint returns a 200 status code"""
    response = client.get('/fortune')
    assert response.status_code == 200

def test_fortune_structure(client):
    """Test if the response structure is a JSON object with 'fortune' key"""
    response = client.get('/fortune')
    json_data = response.get_json()
    assert 'fortune' in json_data

def test_fortune_not_empty(client):
    """Test if the returned fortune is not an empty string"""
    response = client.get('/fortune')
    json_data = response.get_json()
    assert json_data['fortune'] != ''