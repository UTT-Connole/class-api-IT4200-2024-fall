import pytest
from unittest.mock import patch
from flask import Flask
from endpoints.crypto import bitcoin_bp

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
        assert isinstance(response.json['bitcoin_price_usd'], str) 


def test_ethereum_price(client):
    """Test the '/ethereum_price' endpoint for successful response."""
    with patch("endpoints.crypto.requests.get") as mock_get:
        # Mock Coinbase API response for Ethereum
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": {"base": "ETH", "currency": "USD", "amount": "2100.00"}
        }

        response = client.get('/api/ethereum_price')
        assert response.status_code == 200
        assert response.is_json
        assert 'ethereum_price_usd' in response.json
        assert response.json['ethereum_price_usd'] == "2100.00"

def test_ethereum_price_response_format(client):
    """Test that '/ethereum_price' endpoint returns the expected response format."""
    with patch("endpoints.crypto.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": {"base": "ETH", "currency": "USD", "amount": "2100.00"}
        }

        response = client.get('/api/ethereum_price')
        assert response.status_code == 200
        assert response.is_json
        assert 'status' in response.json
        assert 'ethereum_price_usd' in response.json
        assert isinstance(response.json['ethereum_price_usd'], str) 

def test_solana_price(client):
    """Test the '/solana_price' endpoint for successful response."""
    with patch("endpoints.crypto.requests.get") as mock_get:
        # Mock Coinbase API response for Solana
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": {"base": "SOL", "currency": "USD", "amount": "30.00"}
        }

        response = client.get('/api/solana_price')
        assert response.status_code == 200
        assert response.is_json
        assert 'solana_price_usd' in response.json
        assert response.json['solana_price_usd'] == "30.00"

def test_solana_price_response_format(client):
    """Test that '/solana_price' endpoint returns the expected response format."""
    with patch("endpoints.crypto.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": {"base": "SOL", "currency": "USD", "amount": "30.00"}
        }

        response = client.get('/api/solana_price')
        assert response.status_code == 200
        assert response.is_json
        assert 'status' in response.json
        assert 'solana_price_usd' in response.json
        assert isinstance(response.json['solana_price_usd'], str) 


@pytest.fixture
def client():
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
