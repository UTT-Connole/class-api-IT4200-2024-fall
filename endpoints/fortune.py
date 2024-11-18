from flask import Blueprint, jsonify, request
import random
import os
import boto3

fortune_bp = Blueprint('fortune', __name__)

@fortune_bp.route('/fortune', methods=['GET'])
def get_fortune():
    print("Fetching Fortunes from my crystal ball... (AWS DynamoDB)")

    dynamo_url = os.environ.get('DYNAMO_URL') or 'http://localhost:8000'
    dynamo_region = os.environ.get('DYNAMO_REGION') or 'us-west-2'

    print('dynamo_url:', dynamo_url)
    print('dynamo_region:', dynamo_region)

    dynamodb = boto3.resource('dynamodb', endpoint_url=dynamo_url, region_name=dynamo_region)
    table = dynamodb.Table('fortunes')
    
    try:
        response = table.scan()
        fortunes = response['Items']
        # Extract only the 'fortune' attribute
        fortune_texts = [fortune['fortune'] for fortune in fortunes]
        count = request.args.get('count', default=1, type=int)
        if count < 1:
            count = 1
        selected_fortunes = random.sample(fortune_texts, min(count, len(fortune_texts)))
        return jsonify({"fortunes": selected_fortunes})
    except Exception as e:
        print(e)
        return jsonify({"fortunes": "Error fetching fortune"})
