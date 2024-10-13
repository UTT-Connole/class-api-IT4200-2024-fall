def test_fruit_info(client):
    response = client.get('/fruitInfo?fruit=apple')
    assert response.status_code == 200
    data = response.get_json()
    assert data == {
        "fruit": "apple",
        "color": "red",
        "taste": "sweet"
    }
    
    response = client.get('/fruitInfo?fruit=pear')
    assert response.status_code == 404
    data = response.get_json()
    assert data == {"error": "Fruit not found. Please try apple, banana, lemon, orange, grape, or lime."}
