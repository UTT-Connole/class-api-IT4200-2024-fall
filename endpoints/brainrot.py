import random
from flask import Blueprint, jsonify, render_template

# Create a blueprint for brainrot
brainrot_bp = Blueprint('brainrot', __name__)

@brainrot_bp.route('/brainrot', methods=['GET'])
def brainrot():
    words = [
        "Sigma", "Skibidi", "Kai Cenat", "Erm what the Sigma", "Rizz", 
        "Gyatt", "Sussy Sigma", "Sussy Imposter", "Griddy on em"
        ]
    selected_word = random.choice(words)
     # Render the HTML template with the selected word
    return render_template('brainrot.html', brainrot_word=selected_word) 