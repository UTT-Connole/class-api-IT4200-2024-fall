import random
from flask import Blueprint, jsonify

# Create a blueprint for pizza
pizza_bp = Blueprint('pizza', __name__)

@pizza_bp.route('/pizzaToppings', methods=['GET'])
def pizza_toppings():
    sauces = ["Tomato Sauce", "Alfredo Sauce", "Ranch Sauce"]
    toppings = [
        "Pepperoni", "Mushrooms", "Sausage", "Bacon",
        "Extra cheese", "Pineapple", "Spinach"
    ]
    crusts = ["Hand Tossed", "Handmade Pan", "Crunchy Thin Crust"]

    # Randomly choose one sauce, three toppings, and one crust
    selected_sauce = random.choice(sauces)
    selected_toppings = random.sample(toppings, 3)
    selected_crust = random.choice(crusts)

    # Prepare the pizza data
    pizza = {
        "crust": selected_crust,
        "sauce": selected_sauce,
        "toppings": selected_toppings
    }

    # Return the pizza data as JSON
    return jsonify(pizza)
