# def test_get_item(client):
#     # Test for a successful response
#     response = client.get('/item/1')
#     assert response.status_code == 200
#     data = response.get_json()
#     assert data['name'] == 'Item 1'

# def test_item_not_found(client):
#     # Test for item not found
#     response = client.get('/item/999')
#     assert response.status_code == 404
#     assert b'Item not found' in response.data
