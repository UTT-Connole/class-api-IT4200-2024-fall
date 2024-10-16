def test_fortune_status_code(client):
    """Test if the fortune endpoint returns a 200 status code"""
    response = client.get('/fortune')
    assert response.status_code == 200

def test_fortune_structure(client):
    """Test if the response structure is a JSON object with 'fortunes' key"""
    response = client.get('/fortune')
    json_data = response.get_json()
    assert 'fortunes' in json_data

def test_fortune_not_empty(client):
    """Test if the returned fortune is not an empty string"""
    response = client.get('/fortune')
    json_data = response.get_json()
    assert len(json_data['fortunes']) > 0
    assert json_data['fortunes'][0] != ''

def test_fortune_multiple(client):
    """Test if multiple fortunes can be retrieved"""
    response = client.get('/fortune?count=3')
    json_data = response.get_json()
    assert len(json_data['fortunes']) == 3

def test_fortune_invalid_count(client):
    """Test if an invalid count defaults to 1 fortune"""
    response = client.get('/fortune?count=-1')
    json_data = response.get_json()
    assert len(json_data['fortunes']) == 1
