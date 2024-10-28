from unittest.mock import patch

# Test for the random XKCD comic endpoint
@patch('requests.get')  # Mock the requests.get call for the XKCD endpoint
def test_get_random_xkcd_comic(mock_get, client):  # Correct argument order: mock_get comes first
    # Mock a successful response from the XKCD API
    mock_response = {
        'num': 1234,
        'title': 'Test Comic',
        'img': 'https://imgs.xkcd.com/comics/test_comic.png',
        'alt': 'Test comic alt text'
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    # Send a GET request to the random comic endpoint
    response = client.get('/xkcd-comic')
    
    # Check that the status code is 200
    assert response.status_code == 200

    # Check if the correct HTML content is in the response
    assert b'Test Comic' in response.data
    assert b'Test comic alt text' in response.data
    assert b'https://imgs.xkcd.com/comics/test_comic.png' in response.data

# Test for the XKCD comic failure case
@patch('requests.get') # Mock the requests.get call for the XKCD endpoint
def test_xkcd_comic_failure(mock_get, client): # Correct argument order: mock_get comes first
    # Mock a failed response from the XKCD API
    mock_get.return_value.status_code = 404

    # Send a GET request to the random comic endpoint
    response = client.get('/xkcd-comic')

    # Check that the status code is 404
    assert response.status_code == 404

    # Check if the error message is in the response
    assert b'Comic not found' in response.data
