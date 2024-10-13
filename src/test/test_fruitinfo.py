def test_fruit_info_with_valid_fruit(client):
    response = client.get('/fruitInfo?fruit=apple')
    assert response.status_code == 200
    data = response.get_json()
    assert data["fruit"] == "apple"
    assert data["color"] == "red"
    assert data["taste"] == "sweet"

def test_fruit_info_with_invalid_fruit(client):
    response = client.get('/fruitInfo?fruit=unknownfruit')
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Fruit not found. Please try apple, banana, lemon, orange, grape, or lime."

def test_fruit_info_case_insensitive(client):
    response = client.get('/fruitInfo?fruit=Banana')
    assert response.status_code == 200
    data = response.get_json()
    assert data["fruit"] == "Banana"
    assert data["color"] == "yellow"
    assert data["taste"] == "sweet"