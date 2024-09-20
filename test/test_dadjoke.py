import pytest
from app import create_app 

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dadjoke_status_code(client):
    """Test if the dadjoke endpoint returns a 200 status code"""
    response = client.get('/dadjoke')
    assert response.status_code == 200

def test_dadjoke_content_type(client):
    """Test if the dadjoke endpoint returns a response in JSON format"""
    response = client.get('/dadjoke')
    assert response.content_type == 'application/json'

def test_dadjoke_contains_joke(client):
    """Test if the dadjoke endpoint returns a valid joke in the JSON response"""
    response = client.get('/dadjoke')
    json_data = response.get_json()
    assert 'joke' in json_data
    assert isinstance(json_data['joke'], str)
    assert len(json_data['joke']) > 0  # Ensure the joke is not an empty string

# New Tests

def test_dadjoke_multiple_requests(client):
    """Test if multiple requests to the dadjoke endpoint return different jokes"""
    jokes = set()
    for _ in range(10):  # Make 10 requests to the endpoint
        response = client.get('/dadjoke')
        json_data = response.get_json()
        jokes.add(json_data['joke'])  # Add the joke to the set
    
    # There should be more than 1 unique joke in 10 requests
    assert len(jokes) > 1, "The same joke was returned for all requests."

def test_dadjoke_joke_format(client):
    """Test if the joke returned contains no Unicode escape characters like \u2019"""
    response = client.get('/dadjoke')
    json_data = response.get_json()
    joke = json_data['joke']
    
    # Ensure the joke contains no Unicode escape sequences like \u2019
    assert "\\u" not in joke, f"The joke contains Unicode escape characters: {joke}"