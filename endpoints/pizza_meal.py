from flask import Blueprint, jsonify, request
import random

# Define the blueprint
pizza_meal_bp = Blueprint('pizza_meal', __name__)

# Pizza and soda options
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
cheese_levels = ["Light Cheese", "Regular Cheese", "Extra Cheese"]
special_types = ["Regular", "Gluten-Free", "Vegan", "Keto"]

# Soda options and bottle sizes
soda_options = ['Fanta', 'Coca Cola', 'Sprite', 'Mountain Dew', 'Dr. Pepper']
bottle_sizes = ['Personal', '2 Liter']
ice_options = ['With Ice', 'No Ice']

@pizza_meal_bp.route('/pizza_meal', methods=['GET'])
def get_pizza_meal():
    """Return a random pizza and soda selection together as a meal."""

    # Generate pizza details
    selected_sauce = random.choice(sauces)
    selected_toppings = random.sample(toppings, 3)
    selected_crust = random.choice(crusts)
    selected_cheese = request.args.get('cheese', 'Regular Cheese')
    selected_special_type = random.choice(special_types)

    # Check if requested cheese level is valid
    if selected_cheese not in cheese_levels:
        return jsonify({"error": "Invalid cheese level"}), 400

    # Handle half-and-half pizza option
    half_and_half = request.args.get('half_and_half', 'false').lower() == 'true'
    if half_and_half:
        second_toppings = random.sample(toppings, 3)
        pizza = {
            "crust": selected_crust,
            "sauce": selected_sauce,
            "half1_toppings": selected_toppings,
            "half2_toppings": second_toppings,
            "cheese": selected_cheese,
            "special_type": selected_special_type
        }
    else:
        pizza = {
            "crust": selected_crust,
            "sauce": selected_sauce,
            "toppings": selected_toppings,
            "cheese": selected_cheese,
            "special_type": selected_special_type
        }

    # Check for soda 'all' query parameter
    if request.args.get('soda', '').lower() == 'all':
        soda_response = {"sodas": soda_options}
    else:
        # Generate soda details
        selected_soda = random.choice(soda_options)
        selected_size = random.choice(bottle_sizes)
        selected_ice = random.choice(ice_options)
        
        soda_response = {
            "brand": selected_soda,
            "size": selected_size,
            "ice": selected_ice
        }

    # Combine pizza and soda selections in one response
    response = {
        "pizza": pizza,
        "soda": soda_response
    }

    return jsonify(response)
