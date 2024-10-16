def test_get_netflix_shows(client):
    # Send a GET request to /netflix-shows
    response = client.get('/netflix-shows')
    assert response.status_code == 200  # Check if the status code is 200 (OK)
    assert b"netflix_show" in response.data  # Ensure "netflix_show" is present in the response data