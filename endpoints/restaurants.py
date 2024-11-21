import boto3
from flask import Blueprint, jsonify, request, render_template

restaurant_bp = Blueprint('restaurant', __name__)

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')
table_name = "menuItems"

@restaurant_bp.route('/restaurant', methods=['GET'])
def order_food_form():
    return render_template("order.html")

@restaurant_bp.route('/restaurant/menu', methods=['GET'])
def get_menu():
    restaurant = request.args.get('restaurant')

    table = dynamodb.Table(table_name)
    try:
        if restaurant:
            response = table.query(
                IndexName='restaurant-index',
                KeyConditionExpression=boto3.dynamodb.conditions.Key('restaurant').eq(restaurant)
            )
            items = response.get('Items', [])
            if not items:
                return jsonify({"error": "Restaurant not found"}), 404
            return jsonify(items)
        else:
            return jsonify({"error": "Please provide a restaurant name"}), 400
    except dynamodb.meta.client.exceptions.ResourceNotFoundException:
        return jsonify({"error": "Table not found"}), 404

@restaurant_bp.route('/order', methods=['POST'])
def order_food():
    data = request.get_json() if request.is_json else request.form
    restaurant = data.get("restaurant")
    item_ids = data.get("item_ids", [])

    if not item_ids:
        return jsonify({"error": "Please provide at least one item to order"}), 400

    table = dynamodb.Table(table_name)
    try:
        response = table.scan()
        items = response.get('Items', [])
    except dynamodb.meta.client.exceptions.ResourceNotFoundException:
        return jsonify({"error": "Table not found"}), 404

    # Check if the restaurant exists in the items
    if not any(item['restaurant'] == restaurant for item in items):
        return jsonify({"error": "Restaurant not found"}), 404

    ordered_items = [item for item in items if item['id'] in map(str, item_ids)]

    total_price = sum(item['price'] for item in ordered_items)

    return jsonify({
        "restaurant": restaurant,
        "ordered_items": ordered_items,
        "total_price": total_price
    })