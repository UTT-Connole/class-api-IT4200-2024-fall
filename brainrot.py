from flask import Blueprint, jsonify
import random

# Create a blueprint for Random Brainrot
brainrot_bp = Blueprint('brainrot', __name__)

@brainrot_bp.route('/brainrot', methods=['GET'])
def brainrot():
    words = [
        "Sigma", "Skibidi", "Kai Cenat", "Erm what the Sigma", "Rizz", 
        "Gyatt", "Sussy Sigma", "Sussy Imposter", "Griddy on em"
    ]
    selected_word = random.choice(words)
    return jsonify({"word": selected_word})