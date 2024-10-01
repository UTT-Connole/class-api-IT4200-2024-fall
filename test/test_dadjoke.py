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
    """Test if the dadjoke endpoint returns a response in HTML format"""
    response = client.get('/dadjoke')
    assert response.content_type == 'text/html; charset=utf-8'

def test_dadjoke_contains_joke(client):
    """Test if the dadjoke endpoint returns a valid joke in the HTML response"""
    response = client.get('/dadjoke')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert "<p id=\"joke\">" in html_data  # Check if the joke paragraph exists
    assert "Dad Joke of the Day" in html_data  # Check if the heading exists

def test_dadjoke_multiple_requests(client):
    """Test if multiple requests to the dadjoke endpoint return different jokes"""
    jokes = set()
    for _ in range(10):  # Make 10 requests to the endpoint
        response = client.get('/dadjoke')
        html_data = response.get_data(as_text=True)
        
        # Extract the joke from the HTML content using basic string methods or regex
        start_idx = html_data.find('<p id="joke">') + len('<p id="joke">')
        end_idx = html_data.find('</p>', start_idx)
        joke = html_data[start_idx:end_idx].strip()
        
        jokes.add(joke)  # Add the joke to the set
    
    # There should be more than 1 unique joke in 10 requests
    assert len(jokes) > 1, "The same joke was returned for all requests."

def test_dadjoke_joke_format(client):
    """Test if the joke returned contains no Unicode escape characters like \u2019"""
    response = client.get('/dadjoke')
    html_data = response.get_data(as_text=True)

    # Extract the joke from the HTML content
    start_idx = html_data.find('<p id="joke">') + len('<p id="joke">')
    end_idx = html_data.find('</p>', start_idx)
    joke = html_data[start_idx:end_idx].strip()

    # Ensure the joke does not contain Unicode escape characters like \u2019
    assert "\u2019" not in joke, "The joke contains Unicode escape characters."

    
    # Ensure the joke contains no Unicode escape sequences like \u2019
    assert "\\u" not in joke, f"The joke contains Unicode escape characters: {joke}"