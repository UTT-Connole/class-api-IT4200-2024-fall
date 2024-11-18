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
        fortuneselected = random.choice(fortunes)['fortune']
        return jsonify({"fortune": fortuneselected})
    except Exception as e:
        print(e)
        return jsonify({"fortune": "Error fetching fortune"})
