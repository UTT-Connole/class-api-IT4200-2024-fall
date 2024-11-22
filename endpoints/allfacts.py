import os
from flask import Blueprint, jsonify, request
import random
import boto3
from botocore.exceptions import ClientError

allfacts_bp = Blueprint('allfacts', __name__)

FACTS_TABLE_NAME = "facts"

def get_dynamodb_resource():
    dynamo_url = os.environ.get('DYNAMO_URL') or 'http://localhost:8000'
    dynamo_region = os.environ.get('DYNAMO_REGION') or 'us-west-2'
    print('dynamo_url:', dynamo_url)
    print('dynamo_region:', dynamo_region)
    return boto3.resource('dynamodb', endpoint_url=dynamo_url, region_name=dynamo_region)

dynamodb = get_dynamodb_resource()

facts = {
    "random": [
        "Honey never spoils.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries are not.",
        "A day on Venus is longer than a year on Venus.",
        "Sharks have been around longer than trees.",
        "The ocean covers 71 percent of the Earth's surface and the average depth is 12,100 feet."
    ],
    "swimming": [
        "Swimming is one of the best aerobic exercises.",
        "Michael Phelps holds the record for most Olympic gold medals at 23.",
        "The front crawl is the fastest swimming stroke.",
        "Humans have been swimming for thousands of years.",
        "Swimming burns more calories than running."
    ],
    "wrestling": [
        "Hulk Hogan won his first WWF Championship in 1984.",
        "The Undertaker has a 25-2 WrestleMania record.",
        "Stone Cold Steve Austin's 'Austin 3:16' speech revolutionized wrestling promos.",
        "Ric Flair is a 16-time world champion.",
        "Shawn Michaels is known as 'Mr. WrestleMania' for his outstanding performances on the big stage."
    ],
    "tennis": [
        "The fastest serve was 163.7 mph by Sam Groth.",
        "The longest match lasted 11 hours and 5 minutes.",
        "Wimbledon is the oldest tournament.",
        "Yellow tennis balls were introduced in 1972."
    ]
}

def get_facts_by_category(category):
    table = dynamodb.Table(FACTS_TABLE_NAME)
    try:
        response = table.scan(
            FilterExpression=boto3.dynamodb.conditions.Attr('Category').eq(category)
        )
        print(f"Fetched {len(response['Items'])} items for category '{category}'")
        return [item['Fact'] for item in response['Items']]
    except ClientError as e:
        print(f"Error fetching facts: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

@allfacts_bp.route('/allFacts', methods=['GET'])
def all_facts():
    category = request.args.get('category', '').lower()

    if category in facts:
        fact = random.choice(facts[category])
        return jsonify({"category": category, "fact": fact})

    if category:
        category_facts = get_facts_by_category(category)
        if category_facts:
            fact = random.choice(category_facts)
            return jsonify({"category": category, "fact": fact})
        else:
            available_categories = list(facts.keys()) + ['basketball', 'studying']
            message = f"Please choose a valid category. Available categories are: {', '.join(available_categories)}"
            return jsonify({"error": message})

    available_categories = list(facts.keys()) + ['basketball', 'studying']
    message = f"Please choose a valid category. Available categories are: {', '.join(available_categories)}"
    return jsonify({"error": message})