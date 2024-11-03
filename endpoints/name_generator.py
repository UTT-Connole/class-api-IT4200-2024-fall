from flask import Blueprint, request, jsonify
import random

name_bp = Blueprint('name_bp', __name__)

@name_bp.route('/generateName', methods=['GET'])
def generate_name():
    names = {
        "male": ["Jack", "Liam"],
        "female": ["Eve", "Mia"]
    }

    gender = request.args.get('gender', default=None, type=str)
    length = request.args.get('length', default=None, type=int)

    if gender and gender.lower() in names:
        gender_specific_names = names[gender.lower()]
    else:
        gender_specific_names = names["male"] + names["female"]

    if length:
        filtered_names = [name for name in gender_specific_names if len(name) == length]
        if not filtered_names:
            return jsonify({"error": f"No names found with length {length}"}), 400
        name = random.choice(filtered_names)
    else:
        name = random.choice(gender_specific_names)

    return jsonify({"firstname": name})