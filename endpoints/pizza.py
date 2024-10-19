from flask import Blueprint, jsonify, request
import random

# Create a blueprint for pizza
pizza_bp = Blueprint('pizza', __name__)

@pizza_bp.route('/pizza', methods=['GET'])
def pizza():
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
    
    # New Cheese Levels
    cheese_levels = ["Light Cheese", "Regular Cheese", "Extra Cheese"]
    
    # Select random elements
    selected_sauce = random.choice(sauces)
    selected_toppings = random.sample(toppings, 3)
    selected_crust = random.choice(crusts)
    selected_cheese = request.args.get('cheese', 'Regular Cheese')
    
    # Return an error if the cheese level is invalid
    if selected_cheese not in cheese_levels:
        return jsonify({"error": "Invalid cheese level"}), 400  # Use jsonify()

    pizza = {
        "crust": selected_crust,
        "sauce": selected_sauce,
        "toppings": selected_toppings,
        "cheese": selected_cheese  
    }

    return jsonify(pizza)
