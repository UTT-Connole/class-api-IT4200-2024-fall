from flask import Blueprint, jsonify
import random

soda_bp = Blueprint('soda', __name__)

# Soda options
soda_options = ['Fanta', 'Coca Cola', 'Sprite', 'Mountain Dew', 'Dr. Pepper']

@soda_bp.route('/soda', methods=['GET'])
def get_random_soda():
    """Return a random soda brand"""
    selected_soda = random.choice(soda_options)
    return jsonify({'soda': selected_soda})
