
def test_animal_guesser(client):
    """Test the '/animalGuesser' endpoint"""
    response = client.get('/animalGuesser')
    assert response.status_code == 200
    assert response.is_json
    assert 'animal' in response.json

def test_animal_guesser_response_format(client):
    """Test that '/animalGuesser' endpoint returns an animal in the expected format."""
    response = client.get('/animalGuesser')
    assert response.status_code == 200
    assert response.is_json
    assert 'animal' in response.json
    assert response.json['animal'] in ["lion", "tiger", "elephant", "giraffe", "zebra", "panda", "koala"]

def test_animal_guesser_correct_guess(client):
    """Test correct guess response."""
    # Start a game
    response = client.get('/animalGuesser')
    random_animal = response.json['animal']
    
    # correct guess
    response = client.get(f'/animalGuesser?guess={random_animal}')
    assert response.status_code == 200
    assert response.json['result'] == "Correct! You guessed the animal!"

def test_animal_guesser_incorrect_guess(client):
    """Test incorrect guess response."""
    response = client.get('/animalGuesser?user_id=test_user')
    assert response.status_code == 200
    assert response.is_json

    # get random animal from response
    random_animal = response.json['animal']

    # incorrect guess
    guess_response = client.get('/animalGuesser?user_id=test_user&guess=dog')
    assert guess_response.status_code == 200
    assert guess_response.is_json
    assert guess_response.json['result'] == "Incorrect guess"
    assert 'hint' in guess_response.json
    assert guess_response.json['attempts_left'] == 4 - 1


def test_reset_animal_guess(client):
    """Test resetting the animal guess game."""
    response = client.get('/resetAnimalGuess')
    assert response.status_code == 200
    assert response.json['result'] == "Game has been reset. Start a new game!"
    
    #new game can be started after reset
    response = client.get('/animalGuesser')
    assert response.status_code == 200
    assert 'animal' in response.json