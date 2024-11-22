from unittest.mock import patch, MagicMock

def test_get_menu(client):
    # Mock the DynamoDB Table resource
    with patch('endpoints.restaurants.dynamodb.Table') as mock_table:
        mock_table_instance = MagicMock()
        mock_table.return_value = mock_table_instance

        # Mock the query method for a specific restaurant
        mock_table_instance.query.return_value = {
            'Items': [
                {'id': '1', 'restaurant': 'McDonalds', 'name': 'Burger', 'price': 5.99},
                {'id': '2', 'restaurant': 'McDonalds', 'name': 'Fries', 'price': 2.99}
            ]
        }

        # Test for full menu
        response = client.get('/restaurant/menu', query_string={'restaurant': 'McDonalds'})
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) > 0

        # Test for specific restaurant
        response = client.get('/restaurant/menu?restaurant=McDonalds')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert all(item["restaurant"] == "McDonalds" for item in data)

        # Mock the query method for a non-existent restaurant
        mock_table_instance.query.return_value = {'Items': []}

        # Test a non-existent restaurant
        response = client.get('/restaurant/menu?restaurant=NonExistentRestaurant')
        assert response.status_code == 404
        data = response.get_json()
        assert "error" in data
        assert data["error"] == "Restaurant not found"

def test_order_food(client):
    # Mock the DynamoDB Table resource
    with patch('endpoints.restaurants.dynamodb.Table') as mock_table:
        mock_table_instance = MagicMock()
        mock_table.return_value = mock_table_instance

        # Mock the scan method
        mock_table_instance.scan.return_value = {
            'Items': [
                {'id': '1', 'restaurant': 'McDonalds', 'name': 'Burger', 'price': 5.99},
                {'id': '2', 'restaurant': 'McDonalds', 'name': 'Fries', 'price': 2.99}
            ]
        }

        # Test ordering food
        response = client.post('/order', json={"restaurant": "McDonalds", "item_ids": [1]})
        assert response.status_code == 200
        data = response.get_json()
        assert "ordered_items" in data
        assert len(data["ordered_items"]) == 1

        # Test ordering with no items
        response = client.post('/order', json={"restaurant": "McDonalds", "item_ids": []})
        assert response.status_code == 400 
        data = response.get_json()
        assert "error" in data
        assert data["error"] == "Please provide at least one item to order"

        # Mock the scan method for a non-existent restaurant
        mock_table_instance.scan.return_value = {'Items': []}

        # Test ordering from a non-existent restaurant
        response = client.post('/order', json={"restaurant": "NonExistentRestaurant", "item_ids": [1]})
        assert response.status_code == 404
        data = response.get_json()
        assert "error" in data
        assert data["error"] == "Restaurant not found"

        # Test ordering an item that doesn't exist
        response = client.post('/order', json={"restaurant": "McDonalds", "item_ids": [999]})
        assert response.status_code == 404
        data = response.get_json()
        assert "error" in data
        assert data["error"] == "Restaurant not found"