from flask import Blueprint, request, jsonify
import random

animalGuess_bp = Blueprint('animalGuesser', __name__)

game_state = {}

@animalGuess_bp.route('/animalGuesser', methods=['GET'])
def animal_guesser():
    user_id = request.args.get('user_id', 'default_user')
    if user_id not in game_state:
        game_state[user_id] = {
            "animals": ["lion", "tiger", "elephant", "giraffe", "zebra", "panda", "koala"],
            "random_animal": random.choice(["lion", "tiger", "elephant", "giraffe", "zebra", "panda", "koala"]),
            "attempts": 0,
            "max_attempts": 5
        }

    user_game = game_state[user_id]
    random_animal = user_game["random_animal"]
    guess = request.args.get('guess', '').lower()

    user_game["attempts"] += 1

    if guess == random_animal:
        return jsonify({"result": "Correct! You guessed the animal!", "animal": random_animal}), 200
    elif user_game["attempts"] >= user_game["max_attempts"]:
        return jsonify({"result": "Game Over!", "correct_animal": random_animal}), 400
    elif guess:
        hint = f"The animal starts with '{random_animal[0]}'. Try again!"
        return jsonify({"result": "Incorrect guess", "hint": hint, "attempts_left": user_game["max_attempts"] - user_game["attempts"]}), 200
    else:
        return jsonify({"animal": random_animal, "attempts_left": user_game["max_attempts"] - user_game["attempts"]}), 200

@animalGuess_bp.route('/resetAnimalGuess', methods=['GET'])
def reset_animal_guess():
    user_id = request.args.get('user_id', 'default_user')
    if user_id in game_state:
        del game_state[user_id]
    return jsonify({"result": "Game has been reset. Start a new game!"}), 200
