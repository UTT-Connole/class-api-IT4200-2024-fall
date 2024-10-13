
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
