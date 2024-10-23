from flask import Blueprint, jsonify, request
import random

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
    cheese_levels = ["Light Cheese", "Regular Cheese", "Extra Cheese"]
    
    # Half-and-half pizza option
    half_and_half = request.args.get('half_and_half', 'false').lower() == 'true'
    
    # Select random elements for full pizza
    selected_sauce = random.choice(sauces)
    selected_toppings = random.sample(toppings, 3)
    selected_crust = random.choice(crusts)
    selected_cheese = request.args.get('cheese', 'Regular Cheese')

    if selected_cheese not in cheese_levels:
        return jsonify({"error": "Invalid cheese level"}), 400

    if half_and_half:
        second_toppings = random.sample(toppings, 3)
        pizza = {
            "crust": selected_crust,
            "sauce": selected_sauce,
            "half1_toppings": selected_toppings,
            "half2_toppings": second_toppings,
            "cheese": selected_cheese  
        }
    else:
        pizza = {
            "crust": selected_crust,
            "sauce": selected_sauce,
            "toppings": selected_toppings,
            "cheese": selected_cheese  
        }

    return jsonify(pizza)
