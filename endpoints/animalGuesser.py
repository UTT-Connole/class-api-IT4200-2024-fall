from flask import Blueprint, request, jsonify, render_template
import random

animalGuess_bp = Blueprint('animalGuesser', __name__)
game_state = {}

@animalGuess_bp.route('/animalGuesser', methods=['GET'])
def animal_guesser():
    user_id = request.args.get('user_id', 'default_user')
    if user_id not in game_state:
        # Initialize a new game without incrementing attempts
        game_state[user_id] = {
            "animals": ["lion", "tiger", "elephant", "giraffe", "zebra", "panda", "koala"],
            "random_animal": random.choice(["lion", "tiger", "elephant", "giraffe", "zebra", "panda", "koala"]),
            "attempts": 0,
            "max_attempts": 5
        }

    user_game = game_state[user_id]
    random_animal = user_game["random_animal"]
    guess = request.args.get('guess', '').lower()

    if guess:
        user_game["attempts"] += 1

    result = None
    hint = None
    game_over = False
    correct_animal = None

    if guess == random_animal:
        result = "Correct! You guessed the animal!"
        correct_animal = random_animal
    elif user_game["attempts"] >= user_game["max_attempts"]:
        result = "Game Over!"
        game_over = True
        correct_animal = random_animal
    elif guess:
        result = "Incorrect guess"
        hint = f"The animal starts with '{random_animal[0]}'. Try again!"

    # Render the HTML page with game state
    return render_template(
        'animal_guesser.html',
        result=result,
        hint=hint,
        attempts_left=user_game["max_attempts"] - user_game["attempts"],
        game_over=game_over,
        correct_animal=correct_animal
    )