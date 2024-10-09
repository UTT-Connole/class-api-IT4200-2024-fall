import pytest
from app import create_app 
        
#def test_weather_content_type(client):
#    """Test if the weather endpoint returns a response in JSON format"""
#    response = client.get('/weather/Paris')
#    assert response.content_type == 'application/json'
#

def test_weather_error_response(client):
   """Test if the weather endpoint returns a 404 code when no city is given"""
   response = client.get('/weather')
   assert response.status_code == 404

    