def test_sports_fact(client):
    response = client.get('/sports_fact')
    assert response.status_code == 200
    data = response.get_json()
    assert "fact" in data 
    assert isinstance(data['fact'], str) 

def test_sports_fact_with_valid_category(client):
    response = client.get('/sports_fact?category=history')
    assert response.status_code == 200
    data = response.get_json()
    assert "fact" in data
    assert isinstance(data['fact'], str)  
    assert data['fact'] in [
        "Basketball was invented in 1891 by Dr. James Naismith.", 
        "The first modern Olympic Games were held in Athens in 1896."
    ]  

def test_sports_fact_with_invalid_category(client):
    response = client.get('/sports_fact?category=unknown')
    assert response.status_code == 200
    data = response.get_json()
    assert "fact" in data  
    assert isinstance(data['fact'], str)
