
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    # Check for key elements from the template
    assert b"Flask API Explorer" in response.data
    assert b"Explore our available endpoints" in response.data
    assert b"Facts & Information" in response.data
    assert b"Games & Fun" in response.data
    assert b"Utilities" in response.data
    assert b"Other Endpoints" in response.data
