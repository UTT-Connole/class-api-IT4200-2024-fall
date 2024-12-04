import boto3
from flask import Blueprint, jsonify
import requests
from boto3.dynamodb.conditions import Key

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
crypto_table = dynamodb.Table('crypto_prices')

# Create Blueprint
bitcoin_bp = Blueprint("bitcoin", __name__)

def fetch_price_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["data"]["amount"]
    except requests.RequestException as e:
        raise Exception(f"Failed to retrieve price: {str(e)}")

def save_price_to_dynamo(crypto, price):
    crypto_table.put_item(Item={
        "crypto": crypto,
        "price": price
    })

def get_last_price(crypto):
    response = crypto_table.query(
        KeyConditionExpression=Key('crypto').eq(crypto)
    )
    return response['Items'][0]['price'] if response['Items'] else None

@bitcoin_bp.route("/<crypto>_price", methods=["GET"])
def get_crypto_price(crypto):
    crypto_urls = {
        "bitcoin": "https://api.coinbase.com/v2/prices/spot?currency=USD",
        "ethereum": "https://api.coinbase.com/v2/prices/ETH-USD/spot",
        "solana": "https://api.coinbase.com/v2/prices/SOL-USD/spot",
        "cardano": "https://api.coinbase.com/v2/prices/ADA-USD/spot",
        "monero": "https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd"
    }

    if crypto not in crypto_urls:
        return jsonify({"status": "error", "message": "Unsupported cryptocurrency"}), 400

    try:
        # Fetch last saved price from DynamoDB
        last_price = get_last_price(crypto)

        # Attempt to fetch the live price
        try:
            price = fetch_price_from_api(crypto_urls[crypto])

            # Save the new price to DynamoDB
            save_price_to_dynamo(crypto, price)
        except Exception:
            # If API fails, fallback to last saved price
            if last_price:
                return jsonify({
                    "status": "success",
                    "current_price_usd": last_price,
                    "message": "Fetched last saved price as API call failed"
                })
            else:
                raise Exception("API call failed and no saved data available")

        return jsonify({
            "status": "success",
            "current_price_usd": price,
            "last_saved_price_usd": last_price
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
