
from flask import Blueprint, jsonify
import requests

bitcoin_bp = Blueprint("bitcoin", __name__)

@bitcoin_bp.route("/bitcoin_price", methods=["GET"])
def get_bitcoin_price():
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        price = data["data"]["amount"]
        
        return jsonify({
            "status": "success",
            "bitcoin_price_usd": price
        })
        
    except requests.RequestException as e:
        return jsonify({
            "status": "error",
            "message": "Failed to retrieve Bitcoin price",
            "details": str(e)
        }), 500
##ETH endpoint 
@bitcoin_bp.route("/ethereum_price", methods=["GET"])
def get_ethereum_price():
    url = "https://api.coinbase.com/v2/prices/ETH-USD/spot" 
    
    try:
        # Make the API request to Coinbase for Ethereum price
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        price = data["data"]["amount"]
        
        return jsonify({
            "status": "success",
            "ethereum_price_usd": price
        })
        
    except requests.RequestException as e:
        return jsonify({
            "status": "error",
            "message": "Failed to retrieve Ethereum price",
            "details": str(e)
        }), 500
    

@bitcoin_bp.route("/solana_price", methods=["GET"])
def get_solana_price():
    url = "https://api.coinbase.com/v2/prices/SOL-USD/spot" 
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        price = data["data"]["amount"]
        
        return jsonify({
            "status": "success",
            "solana_price_usd": price
        })
        
    except requests.RequestException as e:
        return jsonify({
            "status": "error",
            "message": "Failed to retrieve Solana price",
            "details": str(e)
        }), 500
 