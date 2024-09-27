def test_tennis_fact(client):
    response = client.get('/tennis_fact')
    assert response.status_code == 200
    data = response.get_json()
    assert "fact" in data
    assert isinstance(data['fact'], str)

def test_tennis_fact_with_valid_category(client):
    response = client.get('/tennis_fact?category=history')
    assert response.status_code == 200
    data = response.get_json()
    assert "fact" in data
    assert isinstance(data['fact'], str)  
    assert data['fact'] in [
        "Wimbledon is the oldest tournament.", 
        "Yellow tennis balls were introduced in 1972."
    ]  

def test_tennis_fact_with_invalid_category(client):
    response = client.get('/tennis_fact?category=unknown')
    assert response.status_code == 200
    data = response.get_json()
    assert "fact" in data  
    assert isinstance(data['fact'], str)
