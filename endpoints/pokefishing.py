from flask import Blueprint, jsonify, request
import random
import boto3
from botocore.exceptions import ClientError

pokefishing_bp = Blueprint('pokefishing', __name__)

# Access DynamoDB table
DYNAMODB_ENDPOINT = "http://localhost:8000"
REGION_NAME = "us-west-2"
POKEFISHING_TABLE_NAME = "pokefishing"

# Initialize DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=DYNAMODB_ENDPOINT,
    region_name=REGION_NAME,
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy'
)

def get_table():
    table = dynamodb.Table(POKEFISHING_TABLE_NAME)
    try:
        # Scan the table to retrieve all items
        response = table.scan()
        items = response.get('Items', [])
        
        # Format the output into the desired structure
        formatted_items = [
            {"Id": item.get("Id", ""), "Catch": item.get("Catch", "")} 
            for item in items
        ]
        return formatted_items
    except ClientError as e:
        print(f"Error fetching data: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

@pokefishing_bp.route('/pokefishing', methods=['GET'])
def fish():
    success = random.choice([True, False])
    if success:
        catch = get_table()
        if not catch:  # Handle case where no items are returned
            return jsonify({"message": "No items found in the database"})
        caught_item = random.choice(catch)
        caught = f"You caught: {caught_item['Catch']}!"
    else:
        caught = "You caught: ... Oops, you forgot to reel it in"
    return jsonify({"message": caught})