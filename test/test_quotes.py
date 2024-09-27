def test_quotes_content_type(client):
    """Test if the quotes endpoint returns a response in JSON format"""
    response = client.get('/quotes')
    assert response.content_type.startswith('application/json'), \
        f"Expected content type to start with 'application/json', but got {response.content_type}"

def test_quotes_response_structure(client):
    """Test if the quotes endpoint returns a valid quote structure"""
    response = client.get('/quotes')
    assert response.status_code == 200  # Ensure the request was successful
    json_data = response.get_json()
    
    # Check that the response contains 'author' and 'quote' fields
    assert 'author' in json_data
    assert 'quote' in json_data
    assert isinstance(json_data['author'], str)
    assert isinstance(json_data['quote'], str)
    assert len(json_data['author']) > 0  # Ensure the author is not empty
    assert len(json_data['quote']) > 0  # Ensure the quote is not empty

def test_quotes_uniqueness(client):
    """Test if multiple requests to the quotes endpoint return different quotes"""
    unique_quotes = set()
    for _ in range(10):  # Make 10 requests to the endpoint
        response = client.get('/quotes')
        assert response.status_code == 200  # Ensure the request was successful
        
        json_data = response.get_json()
        quote_tuple = (json_data['author'], json_data['quote'])  # Store the author and quote as a tuple
        unique_quotes.add(quote_tuple)  # Add the quote tuple to the set
    
    # Check if there is at least one unique quote returned
    assert len(unique_quotes) > 0, "No quotes were returned."

    # Ensure there is some variety in the quotes
    assert len(unique_quotes) > 1, "The same quote was returned for all requests." if len(unique_quotes) <= 1 else "Less than 2 unique quotes returned."


def test_quotes_endpoint(client):
    response = client.get('/quotes')
    assert response.status_code == 200
    data = response.get_json()
    assert "quote" in data
    assert "author" in data

def test_quotes_author_exists(client):
    response = client.get('/quotes')
    assert response.status_code == 200
    data = response.get_json()

    # Check if the author is one of the known authors in the list
    valid_authors = ["Marcus Aurelius", "Epictetus", "Seneca", "Plato", "Thorin Oakenshield"]
    assert data["author"] in valid_authors, f"Unexpected author: {data['author']}"
