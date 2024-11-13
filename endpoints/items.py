from flask import Blueprint, jsonify
import json

items_bp = Blueprint('items', __name__)

def load_items_from_file():
    with open('items.json', 'r') as f:
        return json.load(f)

@items_bp.route('/items/<int:min_price>', methods=['GET'])
def get_items(min_price):
    """Fetch and return items with a price greater than or equal to the specified minimum price."""
    items = load_items_from_file()
    filtered_items = [item for item in items if item['price'] >= min_price]

    if not filtered_items:
        return jsonify({'message': 'No items found'}), 404

    return jsonify(filtered_items), 200