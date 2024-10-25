from flask import Blueprint, jsonify, request
import random

soda_bp = Blueprint('soda', __name__)

# Soda options
soda_options = ['Fanta', 'Coca Cola', 'Sprite', 'Mountain Dew', 'Dr. Pepper']

@soda_bp.route('/soda', methods=['GET'])
def get_random_soda():
    """Return a random soda or the full list based on query parameter"""
    if 'all' in request.args and request.args.get('all').lower() == 'true':
        return jsonify({'sodas': soda_options})
    else:
        selected_soda = random.choice(soda_options)
        return jsonify({'soda': selected_soda})
