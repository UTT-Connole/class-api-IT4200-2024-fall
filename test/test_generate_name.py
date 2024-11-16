def test_generate_name(client):
    """Test the '/generateName' endpoint"""
    response = client.get('/generateName')
    assert response.status_code == 200
    data = response.get_json()

    assert "firstname" in data
    assert isinstance(data['firstname'], str)
    assert data['firstname'] in ["Eve", "Jack", "Liam", "Mia"]

def test_generate_name_with_length(client):
    """Test the '/generateName' endpoint with length parameter"""
    response = client.get('/generateName?length=3')
    assert response.status_code == 200
    data = response.get_json()

    assert "firstname" in data
    assert data['firstname'] in ["Eve", "Mia"]

def test_generate_name_with_gender(client):
    """Test the '/generateName' endpoint with gender parameter"""
    response = client.get('/generateName?gender=male')
    assert response.status_code == 200
    data = response.get_json()

    assert "firstname" in data
    assert data['firstname'] in ["Jack", "Liam"]

def test_generate_name_invalid_gender(client):
    """Test the '/generateName' endpoint with an invalid gender"""
    response = client.get('/generateName?gender=unknown')
    assert response.status_code == 200
    data = response.get_json()

    assert "firstname" in data
    assert data['firstname'] in ["Eve", "Jack", "Liam", "Mia"]

def test_generate_name_invalid_length(client):
    """Test the '/generateName' endpoint with an invalid length"""
    response = client.get('/generateName?length=10')
    assert response.status_code == 400
    data = response.get_json()

    assert "error" in data
    assert data["error"] == "No names found with length 10"
