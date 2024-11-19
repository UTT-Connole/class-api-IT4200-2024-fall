from flask import Blueprint, jsonify, request
import random
import os, boto3

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

@pokefishing_bp.route('/pokefishing', methods=['GET'])
def fish():
    success = random.choice([True, False])
    if success:
        caught = table.scan()
    else:
        caught = "... Oops, you forgot to reel it in"
    return jsonify({"You caught": caught + "!"})

    try:
        response = table.scan()
        return jsonify(response['Items']), 200

    except Exception as e:
        print(f"Error accessing DynamoDB: {str(e)}")
        return jsonify({"error": "Failed to access DynamoDB", "details": str(e)}), 500
