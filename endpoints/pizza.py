import random
from flask import Blueprint, jsonify

# Create a blueprint for pizza
pizza_bp = Blueprint('pizza', __name__)

@pizza_bp.route('/pizzaToppings', methods=['GET'])
def pizza_toppings():
    sizes = ["Small", "Medium", "Large"]  # Available pizza sizes
    sauces = ["Tomato Sauce", "Alfredo Sauce", "Ranch Sauce"]
    toppings = [
        {"topping": "Pepperoni"},
        {"topping": "Mushrooms"},
        {"topping": "Sausage"},
        {"topping": "Bacon"},
        {"topping": "Extra cheese"},
        {"topping": "Pineapple"},
        {"topping": "Spinach"}
    ]
    crusts = ["Hand Tossed", "Handmade Pan", "Crunchy Thin Crust"]

    selected_size = random.choice(sizes)  # Select a size at random
    selected_crust = random.choice(crusts)
    selected_sauce = random.choice(sauces)  
    selected_toppings = random.sample(toppings, 3)  # This should correctly choose dictionaries

    # Constructing the pizza dictionary with 'size' at the top
    pizza = {
        "size": selected_size,  
        "crust": selected_crust,
        "sauce": selected_sauce,
        "toppings": selected_toppings
    }

    return jsonify(pizza)
