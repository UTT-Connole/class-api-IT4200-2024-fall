from flask import Flask, request, jsonify, Blueprint
import boto3
import json 

books_bp = Blueprint('books', __name__)

def add_books_endpoint(app):
    @app.route('/books', methods=['GET'])
    def get_books():
        """Fetch books from DynamoDB and return them."""
        print("Fetching books from DynamoDB...")

        dynamo_url = os.environ.get('DYNAMO_URL') or 'http://localhost:8000'
        dynamo_region = os.environ.get('DYNAMO_REGION') or 'us-west-2'

        print('dynamo_url:', dynamo_url)
        print('dynamo_region:', dynamo_region)

        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamo_url, region_name=dynamo_region)

        table = dynamodb.Table('books')

        try:
            # Optional filtering parameters
            genre = request.args.get('genre')
            author = request.args.get('author')

            # Build filter expression dynamically
            filter_expression = None
            expression_attribute_values = {}

            if genre:
                filter_expression = "genre = :g"
                expression_attribute_values[":g"] = genre

            if author:
                if filter_expression:
                    filter_expression += " AND author = :a"
                else:
                    filter_expression = "author = :a"
                expression_attribute_values[":a"] = author

            # Prepare scan parameters
            scan_kwargs = {}
            if filter_expression:
                scan_kwargs['FilterExpression'] = filter_expression
                scan_kwargs['ExpressionAttributeValues'] = expression_attribute_values

            response = table.scan(**scan_kwargs)

            return jsonify(response['Items']), 200

        except Exception as e:
            print(f"Error accessing DynamoDB: {str(e)}")
            return jsonify({"error": "Failed to access DynamoDB", "details": str(e)}), 500
