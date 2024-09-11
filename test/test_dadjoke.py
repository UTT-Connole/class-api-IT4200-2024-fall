import pytest
from app import app_create  # Replace with actual Flask app import

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test 1: Verify that the route returns a 200 status code
def test_dadjoke_status_code(client):
    response = client.get('/dadjoke')
    assert response.status_code == 200

# Test 2: Verify that the response is in JSON format
def test_dadjoke_json_response(client):
    response = client.get('/dadjoke')
    assert response.is_json

# Test 3: Verify that the response contains a joke key
def test_dadjoke_contains_joke_key(client):
    response = client.get('/dadjoke')
    json_data = response.get_json()
    assert 'joke' in json_data

# Test 4: Verify that the joke is one of the predefined jokes
def test_dadjoke_is_from_predefined_list(client):
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I would avoid the sushi if I was you. It’s a little fishy."
        "Today, my son asked 'Can I have a book mark?' and I burst into tears. 11 years old and he still doesn't know my name is Brian. ",
        "I went to the aquarium this weekend, but I didn’t stay long. There’s something fishy about that place.",
        "I gave my handyman a to-do list, but he only did jobs 1, 3, and 5. Turns out he only does odd jobs.",
        "I’m reading a horror story in braille. Something bad is going to happen, I can just feel it."
    ]
    response = client.get('/dadjoke')
    json_data = response.get_json()
    assert json_data['joke'] in jokes

# Test 5: Verify that different jokes are returned across multiple requests
def test_dadjoke_different_responses(client):
    jokes = set()
    for _ in range(10):  # Make 10 requests
        response = client.get('/dadjoke')
        json_data = response.get_json()
        jokes.add(json_data['joke'])
    assert len(jokes) > 1  # Ensure multiple jokes were returned
