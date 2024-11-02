from flask import Blueprint, jsonify, request, render_template

restaurant_bp = Blueprint('restaurant', __name__)

menu_items = [
    {"id": 1, "name": "Burger", "price": 5.99, "restaurant": "McDonalds"},
    {"id": 2, "name": "Fries", "price": 2.99, "restaurant": "McDonalds"},
    {"id": 3, "name": "Soda", "price": 1.00, "restaurant": "McDonalds"},
    {"id": 4, "name": "Salad", "price": 4.99, "restaurant": "Chick Fil A"},
    {"id": 5, "name": "Pizza", "price": 7.99, "restaurant": "Dominos"},
    {"id": 6, "name": "Pasta", "price": 6.99, "restaurant": "Pasta Factory"},
    {"id": 7, "name": "Sandwich", "price": 5.99, "restaurant": "Subway"},
    {"id": 8, "name": "Taco", "price": 3.99, "restaurant": "Taco Bell"},
    {"id": 9, "name": "Burrito", "price": 6.99, "restaurant": "Chipotle"},
    {"id": 10, "name": "Wings", "price": 8.99, "restaurant": "Buffalo Wild Wings"}
]

@restaurant_bp.route('/restaurant', methods=['GET'])
def order_food_form():
   return render_template("order.html")

@restaurant_bp.route('/restaurant/menu', methods=['GET'])
def get_menu():
    restaurant = request.args.get('restaurant')
    if restaurant:
        filtered_menu = [item for item in menu_items if item["restaurant"] == restaurant]
        if not filtered_menu:
            return jsonify({"error": "Restaurant not found"}), 404
        return jsonify(filtered_menu)
    return jsonify(menu_items)

@restaurant_bp.route('/order', methods=['POST'])
def order_food():
    if request.is_json:
        data = request.get_json()
        restaurant = data.get("restaurant")
        item_ids = data.get("item_ids",[])
    else:
        restaurant = request.form.get("restaurant")
        item_ids = request.form.getlist("item_ids")

    available_items = [item for item in menu_items if item["restaurant"] == restaurant]

    if not available_items:
        return jsonify({"error": "Restaurant not found"}), 404

    if len(item_ids) < 1:
        return jsonify({"error": "Please provide at least one item to order"}), 400

    item_ids = [str(item_id) for item_id in item_ids]
    ordered_items = [item for item in available_items if str(item["id"]) in item_ids]
    total_price = sum(item["price"] for item in ordered_items)

    return jsonify({"restaurant": restaurant, "ordered_items": ordered_items, "total_price": total_price})