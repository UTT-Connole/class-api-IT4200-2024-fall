import pytest, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_animal_guesser_page_loads(client):
    """Test that the '/animalGuesser' page loads successfully and returns HTML."""
    response = client.get('/animalGuesser?user_id=test_user')
    assert response.status_code == 200
    assert 'text/html' in response.content_type

def test_incorrect_guess_page_structure(client):
    """Test that the page structure remains correct after an incorrect guess."""
    response = client.get('/animalGuesser?user_id=test_user&guess=wrong_animal')
    assert response.status_code == 200
    # Ensure the feedback section exists in the HTML
    assert b"id=\"feedback\"" in response.data

def test_game_over_page_structure(client):
    """Test that the game over page structure contains necessary elements."""
    user_id = 'game_over_user'

    # Simulate five incorrect guesses
    for _ in range(5):
        response = client.get(f'/animalGuesser?user_id={user_id}&guess=wrong_guess')
        assert response.status_code == 200

    # Check for feedback section, which is used to display game status
    final_response = client.get(f'/animalGuesser?user_id={user_id}&guess=wrong_guess')
    assert final_response.status_code == 200
    assert b"id=\"feedback\"" in final_response.data