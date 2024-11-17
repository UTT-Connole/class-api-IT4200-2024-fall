from flask import Blueprint, jsonify, request
import random

fortune_bp = Blueprint('fortune', __name__)

@fortune_bp.route('/fortune', methods=['GET'])
def get_fortune():
    fortunes = [
        "You will find a fortune.",
        "A fresh start will put you on your way.",
        "Fortune favors the brave.",
        "Good news will come to you by mail.",
        "A beautiful, smart, and loving person will be coming into your life.",
        "A soft voice may be awfully persuasive.",
        "All your hard work will soon pay off."
    ]
    count = request.args.get('count', default=1, type=int)
    if count < 1:
        count = 1
    return jsonify({"fortunes": random.sample(fortunes, min(count, len(fortunes)))})