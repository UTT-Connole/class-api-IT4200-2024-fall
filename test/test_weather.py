import pytest
from app import app  # Import your Flask app
import requests

# Test for valid city response
def test_weather_html_valid_city(mocker):
    # Arrange
    app.config['TESTING'] = True
    client = app.test_client()

    # Mock the API response for a valid city
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "main": {"temp": 72, "humidity": 50},
        "weather": [{"description": "clear sky"}],
        "wind": {"speed": 5}
    }
    mocker.patch('requests.get', return_value=mock_response)

    # Act
    response = client.post('/weather', data={'city': 'London'}, follow_redirects=True)
    html = response.data.decode()

    # Assert
    assert response.status_code == 200
    assert 'background-color: #87CEEB;' in html

#Test for invalid city response
def test_weather_html_invalid_city(mocker):
    # Arrange
    app.config['TESTING'] = True
    client = app.test_client()

    # Mock the API response for an invalid city (404)
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch('requests.get', return_value=mock_response)

    # Act
    response = client.post('/weather', data={'city': 'InvalidCity'}, follow_redirects=True)

    # Assert
    assert response.status_code == 404
    assert b'City not found or API error.' in response.data