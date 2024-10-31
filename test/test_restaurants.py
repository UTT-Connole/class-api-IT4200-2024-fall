def test_get_menu(client):
    response = client.get('/restaurant')
    assert response.status_code == 200
    data = response.get_json()
    assert "menu" in data
    assert len(data["menu"]) > 0

def test_order_food(client):
    response = client.post('/order', json={"item_ids": [1, 2, 3]})
    assert response.status_code == 200
    data = response.get_json()
    assert "ordered_items" in data
    assert "total_price" in data
    assert len(data["ordered_items"]) == 3
    assert data["total_price"] == 10.97

    response = client.post('/order', json={"item_ids": [999]})
    assert response.status_code == 200 
    data = response.get_json()
    assert len(data["ordered_items"]) == 0
    assert data["total_price"] == 0.0