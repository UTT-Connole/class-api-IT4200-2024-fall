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
    if restaurant:
        response = table.scan(
            FilterExpression="restaurant = :r",
            ExpressionAttributeValues={":r": restaurant}
        )
        items = response.get('Items', [])
        if not items:
            return jsonify({"error": "Restaurant not found"}), 404
        return jsonify(items)

    response = table.scan()
    return jsonify(response.get('Items', []))

@restaurant_bp.route('/order', methods=['POST'])
def order_food():
    data = request.get_json() if request.is_json else request.form
    restaurant = data.get("restaurant")
    item_ids = data.get("item_ids", [])

    table = dynamodb.Table(table_name)
    response = table.scan(
        FilterExpression="restaurant = :r",
        ExpressionAttributeValues={":r": restaurant}
    )
    available_items = response.get('Items', [])

    if not available_items:
        return jsonify({"error": "Restaurant not found"}), 404

    if len(item_ids) < 1:
        return jsonify({"error": "Please provide at least one item to order"}), 400

    ordered_items = [item for item in available_items if str(item["id"]) in item_ids]
    total_price = sum(item["price"] for item in ordered_items)

    return jsonify({"restaurant": restaurant, "ordered_items": ordered_items, "total_price": total_price})