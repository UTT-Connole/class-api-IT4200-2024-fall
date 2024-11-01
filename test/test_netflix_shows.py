def test_get_netflix_shows(client):
    # Send a GET request to /netflix-shows
    response = client.get('/netflix-shows')
    assert response.status_code == 200  # Check if the status code is 200 (OK)
    assert b"netflix_show" in response.data  # Ensure "netflix_show" is present in the response data
    data = response.get_json()
    assert isinstance(data['netflix_show'], dict)  # Ensure the returned show is a dictionary
    assert 'title' in data['netflix_show']  # Check if 'title' is in the response
    assert 'fact' in data['netflix_show']  # Check if 'fact' is in the response

def test_get_netflix_show_by_title(client):
    """Test filtering Netflix shows by title"""
    response = client.get('/netflix-shows?title=Stranger')
    assert response.status_code == 200  # Check if the status code is 200 (OK)
    data = response.get_json()
    assert 'netflix_show' in data  # Ensure "netflix_show" is present in the response data
    assert data['netflix_show']['title'] == "Stranger Things"  # Verify the title matches

def test_get_netflix_show_by_nonexistent_title(client):
    """Test retrieving a show with a title that does not exist"""
    response = client.get('/netflix-shows?title=NonexistentShow')
    assert response.status_code == 404  # Check if the status code is 404 (Not Found)
    data = response.get_json()
    assert 'error' in data  # Ensure an error message is present
    assert data['error'] == "No shows found with the specified title."  # Check the error message