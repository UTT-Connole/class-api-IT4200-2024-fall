from flask import Flask, request, jsonify
import random
import matplotlib

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/calc', methods=['GET','POST'])
def calc_main():
    x = request.args.get('x')
    y = request.args.get('y')
    if x and y:
        x = int(x)
        y = int(y)
        result = x+y
    else:
        result = "Invalid Input"
    return str(result)

@app.route('/color', methods=['GET','POST'])
def color_hexifier():
    color_name = request.args.get('color')
    
    print(f"Received color name: {color_name}")
    
    if color_name and color_name.lower() in matplotlib.colors.CSS4_COLORS:
        hex_code = matplotlib.colors.CSS4_COLORS[color_name.lower()]
        return f"The hex code for {color_name} is {hex_code}"
    else:
        return "Invalid color name"

@app.route('/twoManaCombos', methods=['GET'])
def random_combo():
    two_m =[{ "name": "Boros", "color_1": "red", "color_2": "white"},
            { "name": "Golgari", "color_1": "blue", "color_2": "black"},
            { "name": "Gruul", "color_1": "red", "color_2": "green"},
            { "name": "Orzhov", "color_1": "white", "color_2": "black"},
            { "name": "Rakdos", "color_1": "black", "color_2": "red"},
            { "name": "Selesnya", "color_1": "white", "color_2": "green"}]
    r = two_m[random.randrange(len(two_m))]
    return r
print(random_combo())

@app.route('/quotes', methods=['GET'])
def fav_quotes():
    quotes = [
    {"author": "Marcus Aurelius", "quote": "You have power over your mind - not outside events. Realize this, and you will find strength."},
    {"author": "Marcus Aurelius", "quote": "The happiness of your life depends upon the quality of your thoughts."},
    {"author": "Epictetus", "quote": "It's not what happens to you, but how you react to it that matters."},
    {"author": "Seneca", "quote": "We suffer more in imagination than in reality."},
    {"author": "Marcus Aurelius", "quote": "Waste no more time arguing about what a good man should be. Be one."},
    {"author": "Epictetus", "quote": "No man is free who is not master of himself."},
    {"author": "Seneca", "quote": "Luck is what happens when preparation meets opportunity."}
]
    quote = random.choice(quotes)
    return jsonify(quote)

@app.route('/randomName', methods=['GET'])
def random_name():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    name = random.choice(names)
    return jsonify({"name": name})

@app.route('/pizzaToppings', methods=['GET'])
def pizza_toppings():
    toppings = [
        {"topping": "Pepperoni"},
        {"topping": "Mushrooms"},
        {"topping": "Chicken"},
        {"topping": "Sausage"},
        {"topping": "Bacon"},
        {"topping": "Extra cheese"},
        {"topping": "Pineapple"},
        {"topping": "Spinach"}
    ]
    selected_toppings = random.sample(toppings, 3) 
    return jsonify(selected_toppings)

@app.route('/dadjoke', methods=['GET'])
def dad_joke():
    jokes = [
        {"Why don't skeletons fight each other? They don't have the guts."},
        {"What do you call fake spaghetti? An impasta!"},
        {"Why did the scarecrow win an award? Because he was outstanding in his field!"},
        {"I would avoid the sushi if I was you. It’s a little fishy."}
    ]
    joke = random.choice(jokes)
    return jsonify({"joke": joke})


