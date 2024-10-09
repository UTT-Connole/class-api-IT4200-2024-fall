
def test_animal_guesser(client):
    """Test the '/animalGuesser' endpoint"""
    response = client.get('/animalGuesser')
    assert response.status_code == 200
    assert response.is_json
    assert 'animal' in response.json
