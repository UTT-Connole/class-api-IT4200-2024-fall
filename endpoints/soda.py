from flask import Blueprint, jsonify, request
import random

soda_bp = Blueprint('soda', __name__)

# Soda options, bottle sizes, and simple ice options
soda_options = ['Fanta', 'Coca Cola', 'Sprite', 'Mountain Dew', 'Dr. Pepper']
bottle_sizes = ['Personal', '2 Liter']
ice_options = ['Ice', 'No Ice']

@soda_bp.route('/soda', methods=['GET'])
def get_random_soda():
    """Return a random soda with a bottle size and ice option, or the full list based on query parameter"""
    
    if 'all' in request.args and request.args.get('all').lower() == 'true':
        return jsonify({'sodas': soda_options})
    
    # Randomly select soda, bottle size, and ice option
    selected_soda = random.choice(soda_options)
    selected_size = random.choice(bottle_sizes)
    selected_ice = random.choice(ice_options)
    
    return jsonify({'soda': selected_soda, 'size': selected_size, 'ice': selected_ice})
