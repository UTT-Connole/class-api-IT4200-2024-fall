from flask import Blueprint, jsonify, request
import random

soda_bp = Blueprint('soda', __name__)

# Soda options and bottle sizes
soda_options = ['Fanta', 'Coca Cola', 'Sprite', 'Mountain Dew', 'Dr. Pepper']
bottle_sizes = ['Personal', '2 Liter']

@soda_bp.route('/soda', methods=['GET'])
def get_random_soda():
    """Return a random soda with a bottle size or the full list based on query parameter"""
    if 'all' in request.args and request.args.get('all').lower() == 'true':
        return jsonify({'sodas': soda_options})
    else:
        selected_soda = random.choice(soda_options)
        selected_size = random.choice(bottle_sizes)
        return jsonify({'soda': selected_soda, 'size': selected_size})
