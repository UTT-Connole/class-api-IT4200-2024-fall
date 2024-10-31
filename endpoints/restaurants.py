from flask import Blueprint, jsonify, request, render_template

restaurant_bp = Blueprint('restaurant', __name__)

menu_items = [
    {"id": 1, "name": "Burger", "price": 5.99},
    {"id": 2, "name": "Fries", "price": 2.99},
    {"id": 3, "name": "Soda", "price": 1.99},
    {"id": 4, "name": "Salad", "price": 4.99},
    {"id": 5, "name": "Pizza", "price": 7.99},
    {"id": 6, "name": "Pasta", "price": 6.99},
    {"id": 7, "name": "Sandwich", "price": 5.99},
    {"id": 8, "name": "Taco", "price": 3.99},
    {"id": 9, "name": "Burrito", "price": 6.99},
    {"id": 10, "name": "Wings", "price": 8.99}
]

@restaurant_bp.route('/restaurant', methods=['GET'])
def get_menu():
    return jsonify({"menu": menu_items})

@restaurant_bp.route('/order', methods=['POST'])
def order_food():
    data = request.get_json()
    item_ids = data.get("item_ids", [])

    ordered_items = [item for item in menu_items if item["id"] in item_ids]
    total_price = sum(item["price"] for item in ordered_items)

    return jsonify({"ordered_items": ordered_items, "total_price": total_price})