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
    response = client.get('/weather/London')

    # Assert
    assert response.status_code == 200

# Test for invalid city response
def test_weather_html_invalid_city(mocker):
    # Arrange
    app.config['TESTING'] = True
    client = app.test_client()

    # Mock the API response for an invalid city (404)
    mocker.patch('requests.get').return_value.status_code = 404

    # Act
    response = client.get('/weather_html/InvalidCity')

    # Assert
    assert response.status_code == 404
