# def test_get_items_with_min_price(client):

#     """Test the '/items' endpoint with a minimum price"""
#     response = client.get('/items?min_price=5')
#     assert response.status_code == 200
#     assert response.is_json
#     assert isinstance(response.json, list)
#     assert len(response.json) > 0  # Ensure at least one item is returned

# def test_get_items_no_results(client):
    
#     """Test the '/items' endpoint with a minimum price that returns no items"""
#     response = client.get('/items?min_price=100')  # Assuming no items with this price
#     assert response.status_code == 404
#     assert response.is_json
#     assert response.json['message'] == 'No items found'
from app import create_app

def test_items_json(client):
    """Test to see if the items endpoint returns a JSON format"""
    response = client.get('/items/0')
    assert response.content_type == 'application/json'
