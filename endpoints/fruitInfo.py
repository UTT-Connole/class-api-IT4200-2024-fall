from flask import Blueprint, request, jsonify
import json
import os

fruit_bp = Blueprint('fruit', __name__)

@fruit_bp.route('/fruitInfo', methods=['GET', 'POST'])
def fruit_info():
    try:
        fruits_path = os.path.join(os.path.dirname(__file__), '..', 'fruits.json')
        with open(fruits_path, 'r') as f:
            fruits = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        fruits = {}

    if request.method == 'GET':
        fruit_name = request.args.get('fruit')
        if fruit_name:
            fruit_name_lower = fruit_name.lower()
            if fruit_name_lower in fruits:
                info = fruits[fruit_name_lower]
                return jsonify({
                    "fruit": fruit_name_lower,
                    "color": info["color"],
                    "taste": info["taste"]
                })
            else:
                available_fruits = ', '.join(fruits.keys())
                return jsonify({"error": f"Fruit not found. Available fruits: {available_fruits}."}), 404
        else:
            return jsonify(fruits), 200

    elif request.method == 'POST':
        new_fruit = request.args.get('fruit')
        new_color = request.args.get('color')
        new_taste = request.args.get('taste')

        if new_fruit and new_color and new_taste:
            fruits[new_fruit.lower()] = {
                "color": new_color,
                "taste": new_taste
            }
            with open(fruits_path, 'w') as f:
                json.dump(fruits, f, indent=4)
            return jsonify({"message": f"{new_fruit} added successfully!"}), 201
        else:
            return jsonify({"error": "Invalid data. Please provide fruit name, color, and taste."}), 400
