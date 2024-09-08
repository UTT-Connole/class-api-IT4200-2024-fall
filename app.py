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
    op = request.args.get('op')
    if x and y and op:
        x = int(x)
        y = int(y)
    else:
        result = "Invalid Input"
    if op == 'add':
        result = x + y
    elif op == 'subtract':
        result = x - y
    elif op == 'multiply':
        result = x * y
    elif op == 'divide':
        if y != 0:
            result = x / y
        else:
            result = "You cannot divide by 0"
    else:
        result = "You might have spelled something wrong"
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
"""print(random_combo()) <-Quoting this out because not really needed? Test it with the route!"""

@app.route('/quotes', methods=['GET'])
def fav_quotes():
    quotes = [
    {"author": "Marcus Aurelius", "quote": "You have power over your mind - not outside events. Realize this, and you will find strength."},
    {"author": "Marcus Aurelius", "quote": "The happiness of your life depends upon the quality of your thoughts."},
    {"author": "Epictetus", "quote": "It's not what happens to you, but how you react to it that matters."},
    {"author": "Seneca", "quote": "We suffer more in imagination than in reality."},
    {"author": "Marcus Aurelius", "quote": "Waste no more time arguing about what a good man should be. Be one."},
    {"author": "Epictetus", "quote": "No man is free who is not master of himself."},
    {"author": "Seneca", "quote": "Luck is what happens when preparation meets opportunity."},
    {"author": "Thorin Oakenshield", "quote": "If more of us valued food and cheer and song above hoarded gold, it would be a merrier world."}
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
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I would avoid the sushi if I was you. It’s a little fishy."
        "Today, my son asked 'Can I have a book mark?' and I burst into tears. 11 years old and he still doesn't know my name is Brian. "
        "I went to the aquarium this weekend, but I didn’t stay long. There’s something fishy about that place."
        "I gave my handyman a to-do list, but he only did jobs 1, 3, and 5. Turns out he only does odd jobs."
        "I’m reading a horror story in braille. Something bad is going to happen, I can just feel it."
    ]
    joke = random.choice(jokes)
    return jsonify({"joke": joke})

@app.route('/travel', methods=['GET','POST'])
def travel():
    destinations = [
        "Paris, France",
        "Rome, Italy",
        "Maui, Hawaii",
        "London, England",
        "Tokyo, Japan",
        "Barcelona, Spain",
        "New York City, New York",
        "Los Angeles, California",
        "Dublin, Ireland",
        "Cairo, Egypt",
        "Sydney, Australia",
        "Sacramento, California",
        "Salt Lake, Utah",
        "Denver, Colorado",
        "Santa Cruise, California",
        "London, England"
        ]
    picked = random.choice(destinations)
    return jsonify({"You should go to": picked})

@app.route('/marathonFacts', methods=['GET'])
def marathon_facts():
    facts = [
        {"fact": "The first marathon was in 1896 during the Athens Olympics.", "category": "history"},
        {"fact": "The official marathon distance is 26.2 miles (42.195 km).", "category": "distance"},
        {"fact": "The fastest marathon time for men is 2:01:39.", "category": "records"},
        {"fact": "The fastest marathon time for women is 2:14:04.", "category": "records"},
        {"fact": "Eliud Kipchoge ran a marathon in under 2 hours in a special event.", "category": "milestones"},
        {"fact": "Over 50,000 runners finish the New York City Marathon each year.", "category": "participation"}
    ]
    
    random_fact = random.choice(facts)
    return jsonify(random_fact)

@app.route('/favoritequote', methods=['GET'])
def get_favorite_quote():
    favorite_quote = {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs"
    }
    return jsonify(favorite_quote)

if __name__ == '__main__':
    app.run(debug=True)

    picked = random.choice(destinations)

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/fortune', methods=['GET'])
def get_fortune():
    fortunes = [
        "You will find a fortune.",
        "A fresh start will put you on your way.",
        "Fortune favors the brave.",
        "Good news will come to you by mail."
    ]
    return jsonify({"fortune": random.choice(fortunes)})

if __name__ == '__main__':
    app.run(debug=True)
#    return jsonify({"You should go to": picked})

@app.route('/tennisFacts', methods=['GET'])
def tennis_facts_endpoint():
    tennis_facts = [
        {"fact": "The longest tennis match lasted 11 hours and 5 minutes at Wimbledon in 2010.", "category": "records"},
        {"fact": "The US Open is played on hard courts.", "category": "tournaments"},
        {"fact": "Serena Williams has 23 Grand Slam singles titles.", "category": "players"},
        {"fact": "Roger Federer, Rafael Nadal, and Novak Djokovic each have 20 Grand Slam titles.", "category": "players"},
        {"fact": "'Love' in tennis means zero, from the French 'l'oeuf' meaning egg.", "category": "terminology"},
        {"fact": "Wimbledon is the oldest tennis tournament, started in 1877.", "category": "history"}
    ]
    return jsonify(random.choice(tennis_facts))