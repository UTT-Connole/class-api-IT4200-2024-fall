def test_get_motivation(client):
    
    """Test the '/motivation' endpoint"""
    response = client.get('/motivation')
    assert response.status_code == 200
    assert response.is_json
    assert 'motivational_quote' in response.json
    assert isinstance(response.json['motivational_quote'], str)
