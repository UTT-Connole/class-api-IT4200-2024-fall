import pytest
from unittest.mock import patch
from flask import Flask
from endpoints.crypto import bitcoin_bp  # Make sure this matches the actual Blueprint name

def test_bitcoin_price(client):
    """Test the '/bitcoin_price' endpoint for successful response."""
    with patch("endpoints.crypto.requests.get") as mock_get:
        # Mock Coinbase API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": {"base": "BTC", "currency": "USD", "amount": "34250.87"}
        }

        response = client.get('/api/bitcoin_price')
        assert response.status_code == 200
        assert response.is_json
        assert 'bitcoin_price_usd' in response.json
        assert response.json['bitcoin_price_usd'] == "34250.87"

def test_bitcoin_price_response_format(client):
    """Test that '/bitcoin_price' endpoint returns the expected response format."""
    with patch("endpoints.crypto.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": {"base": "BTC", "currency": "USD", "amount": "34250.87"}
        }

        response = client.get('/api/bitcoin_price')
        assert response.status_code == 200
        assert response.is_json
        assert 'status' in response.json
        assert 'bitcoin_price_usd' in response.json
        assert isinstance(response.json['bitcoin_price_usd'], str)  # Price should be a string


@pytest.fixture
def client():
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
