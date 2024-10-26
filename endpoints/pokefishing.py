from flask import Blueprint, jsonify, request
import random

pokefishing_bp = Blueprint('pokefishing', __name__)

magikarp = [
    "a regular ol' Magikarp",
    "a calico pattern Magikarp",
    "a orange two-tone pattern Magikarp",
    "a pink dapple pattern Magikarp",
    "a gray diamond pattern Magikarp",
    "a purple patches pattern Magikarp",
    "a apricot tiger pattern Magikarp",
    "a brown stripes pattern Magikarp",
    "a orange forehead pattern Magikarp",
    "a blue raindrops pattern Magikarp",
    "a shiny Magikarp",
    "a... Oh no, it's a Gyarados!!",
    "a Goldeen and it's the biggest you've ever seen",
    "nothing... But you did see a Mudkip riding on a Lotad"
]

@pokefishing_bp.route('/pokefishing', methods=['GET'])
def fish():
    success = random.choice([True, False])
    if success:
        caught = random.choice(magikarp)
    else:
        caught = "... Oops, you forgot to reel it in"
    return jsonify({"You caught": caught + "!"})