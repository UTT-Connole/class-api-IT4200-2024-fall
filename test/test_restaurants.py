def test_get_menu(client):
    # test for full menu
    response = client.get('/restaurant/menu')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

    # test for specific restaurant
    response = client.get('/restaurant/menu?restaurant=McDonalds')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert all(item["restaurant"] == "McDonalds" for item in data)

    # Test a non-existent restaurant
    response = client.get('/restaurant/menu?restaurant=NonExistentRestaurant')
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Restaurant not found"

def test_order_food(client):
    response = client.post('/order', json={"restaurant": "McDonalds", "item_ids": [1]})
    assert response.status_code == 200
    data = response.get_json()
    assert "ordered_items" in data
    assert "total_price" in data
    assert len(data["ordered_items"]) == 1
    expected_price = sum(item["price"] for item in data["ordered_items"])
    assert data["total_price"] == expected_price

    response = client.post('/order', json={"restaurant": "McDonalds", "item_ids": []})
    assert response.status_code == 400 
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Please provide at least one item to order"

    response = client.post('/order', json={"restaurant": "NonExistentRestaurant", "item_ids": [1]})
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Restaurant not found"

    response = client.post('/order', json={"restaurant": "McDonalds", "item_ids": [999]})
    assert response.status_code == 200
    data = response.get_json()
    assert "ordered_items" in data
    assert "total_price" in data
    assert len(data["ordered_items"]) == 0
    assert data["total_price"] == 0.0