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
    
    # Cheese Levels
    cheese_levels = ["Light Cheese", "Regular Cheese", "Extra Cheese"]
    
    # Function to create a single pizza
    def create_pizza():
        selected_sauce = random.choice(sauces)
        selected_toppings = random.sample(toppings, 3)
        selected_crust = random.choice(crusts)
        selected_cheese = request.args.get('cheese', 'Regular Cheese')

        if selected_cheese not in cheese_levels:
            return {"error": "Invalid cheese level"}, 400

        return {
            "crust": selected_crust,
            "sauce": selected_sauce,
            "toppings": selected_toppings,
            "cheese": selected_cheese
        }

    # RNG to determine if user gets one or two pizzas
    pizza_count = random.choice([1, 2])

    if pizza_count == 1:
        return jsonify(create_pizza())
    else:
        return jsonify([create_pizza(), create_pizza()])
