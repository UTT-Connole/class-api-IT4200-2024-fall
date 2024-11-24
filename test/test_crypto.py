import pytest
from unittest.mock import patch


@pytest.fixture
def client():
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_bitcoin_price(client):
    """Test the '/bitcoin_price' endpoint for successful response."""
    with patch("endpoints.crypto.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": {"base": "BTC", "currency": "USD", "amount": "34250.87"}
        }

        response = client.get('/api/bitcoin_price')
        assert response.status_code == 200
        assert response.is_json
        assert 'status' in response.json, "Response should contain 'status'."
        assert 'current_price_usd' in response.json, "Response should contain 'current_price_usd'."
        assert 'last_saved_price_usd' in response.json, "Response should contain 'last_saved_price_usd'."
        assert response.json['current_price_usd'] == "34250.87"
        assert response.json['last_saved_price_usd'] == "34250.87"


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
        assert 'status' in response.json, "Response should contain 'status'."
        assert 'current_price_usd' in response.json, "Response should contain 'current_price_usd'."
        assert 'last_saved_price_usd' in response.json, "Response should contain 'last_saved_price_usd'."
        assert isinstance(response.json['current_price_usd'], str)


def test_ethereum_price(client):
    """Test the '/ethereum_price' endpoint for successful response."""
    with patch("endpoints.crypto.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": {"base": "ETH", "currency": "USD", "amount": "2100.00"}
        }

        response = client.get('/api/ethereum_price')
        assert response.status_code == 200
        assert response.is_json
        assert 'status' in response.json, "Response should contain 'status'."
        assert 'current_price_usd' in response.json, "Response should contain 'current_price_usd'."
        assert 'last_saved_price_usd' in response.json, "Response should contain 'last_saved_price_usd'."
        assert response.json['current_price_usd'] == "2100.00"
        assert response.json['last_saved_price_usd'] == "2100.00"


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
        assert 'status' in response.json, "Response should contain 'status'."
        assert 'current_price_usd' in response.json, "Response should contain 'current_price_usd'."
        assert 'last_saved_price_usd' in response.json, "Response should contain 'last_saved_price_usd'."
        assert isinstance(response.json['current_price_usd'], str)


def test_solana_price(client):
    """Test the '/solana_price' endpoint for successful response."""
    with patch("endpoints.crypto.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": {"base": "SOL", "currency": "USD", "amount": "30.00"}
        }

        response = client.get('/api/solana_price')
        assert response.status_code == 200
        assert response.is_json
        assert 'status' in response.json, "Response should contain 'status'."
        assert 'current_price_usd' in response.json, "Response should contain 'current_price_usd'."
        assert 'last_saved_price_usd' in response.json, "Response should contain 'last_saved_price_usd'."
        assert response.json['current_price_usd'] == "30.00"
        assert response.json['last_saved_price_usd'] == "30.00"


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
        assert 'status' in response.json, "Response should contain 'status'."
        assert 'current_price_usd' in response.json, "Response should contain 'current_price_usd'."
        assert 'last_saved_price_usd' in response.json, "Response should contain 'last_saved_price_usd'."
        assert isinstance(response.json['current_price_usd'], str)
