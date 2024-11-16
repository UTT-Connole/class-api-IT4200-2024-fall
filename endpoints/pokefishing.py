from flask import Blueprint, jsonify, request
import random
import os, boto3

pokefishing_bp = Blueprint('pokefishing', __name__)

# Access DynamoDB table
dynamo_url = os.environ.get('DYNAMO_URL') or 'http://localhost:8000'
dynamo_region = os.environ.get('DYNAMO_REGION') or 'us-west-2'
print('dynamo_url:', dynamo_url)
print('dynamo_region:', dynamo_region)
dynamodb = boto3.resource('dynamodb', endpoint_url=dynamo_url, region_name=dynamo_region)
table = dynamodb.Table('pokefishing')

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
