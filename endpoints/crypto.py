# endpoints/bitcoin.py

from flask import Blueprint, jsonify
import requests

bitcoin_bp = Blueprint("bitcoin", __name__)

@bitcoin_bp.route("/bitcoin_price", methods=["GET"])
def get_bitcoin_price():
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    
    try:
        # Make the API request to Coinbase
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        price = data["data"]["amount"]
        
        # Return the price in a JSON response
        return jsonify({
            "status": "success",
            "bitcoin_price_usd": price
        })
        
    except requests.RequestException as e:
        #request errors
        return jsonify({
            "status": "error",
            "message": "Failed to retrieve Bitcoin price",
            "details": str(e)
        }), 500
