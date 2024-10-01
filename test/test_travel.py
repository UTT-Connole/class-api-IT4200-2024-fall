from app import create_app 

def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
def test_travel_content_type(client):
    """Test if the travel endpoint returns a response in JSON format"""
    response = client.get('/travel')
    assert response.content_type == 'application/json'

def test_travel_contains_valid_response(client):
    """Test if the travel endpoint returns a valid travel location in the JSON response"""
    response = client.get('/travel')
    json_data = response.get_json()
    assert 'You should go to' in json_data
    assert isinstance(json_data['You should go to'], str)
    assert len(json_data['You should go to']) > 0  # Ensure the travel location response is not an empty string

def test_travel_contains_flight_time(client):
    """Test if the travel endpoint returns a flight time in JSON format"""
    response = client.get('/travel')
    json_data = response.get_json()
    assert 'To fly from SLC it will take ' in json_data
    assert isinstance(json_data['To fly from SLC it will take '], str)
    assert len(json_data['To fly from SLC it will take ']) > 0 






    
    