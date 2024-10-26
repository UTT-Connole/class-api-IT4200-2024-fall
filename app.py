from flask import Flask, request, jsonify, render_template
from endpoints.readme import readme_bp
from endpoints.marathonfacts import marathonFacts_bp
from endpoints.dadjoke import dadjoke_bp
from endpoints.brainrot import brainrot_bp
from endpoints.math import math_bp
from endpoints.motivation import motivation_bp
from endpoints.math import math_bp
from endpoints.mtg import mtg_bp
from endpoints.allfacts import allfacts_bp
from endpoints.pizza import pizza_bp
from endpoints.soda import soda_bp
from endpoints.version import version_bp
from endpoints.quotes import quotes_bp
from endpoints.photogallery import photogallery_bp
from endpoints.pokefishing import pokefishing_bp
import random, requests
import os, json
import time
from decimal import Decimal, getcontext 
import matplotlib, math

def load_items_from_file():
    with open('items.json', 'r') as f:
        return json.load(f)
    


def create_app():
    app = Flask(__name__)

    app.register_blueprint(readme_bp)
    app.register_blueprint(brainrot_bp)
    app.register_blueprint(dadjoke_bp)
    app.register_blueprint(math_bp)
    app.register_blueprint(allfacts_bp)
    app.register_blueprint(marathonFacts_bp)
    app.register_blueprint(mtg_bp)
    app.register_blueprint(motivation_bp)
    app.register_blueprint(photogallery_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(pokefishing_bp)
    app.register_blueprint(soda_bp)
    app.register_blueprint(version_bp)
    app.register_blueprint(quotes_bp)

    @app.route('/generateName', methods=['GET'])
    def generate_name():
        names = ["Eve", "Jack", "Liam", "Mia"]
        length = request.args.get('length', default=None, type=int)
    
        if length:
            filtered_names = [name for name in names if len(name) == length]
            if not filtered_names:
                return jsonify({"error": f"No names found with length {length}"}), 400
            name = random.choice(filtered_names)
        else:
            name = random.choice(names)
    
        return jsonify({"firstname": name})

    
    @app.route('/greet', methods=['GET'])
    def greet():
        name = request.args.get('name')
        if name:
            return jsonify({"message": f"Hello, {name}!"})
        return jsonify({"message": "Hello, Welcome to the API!"})
        
    @app.route('/')
    def hello_world():
        return render_template('index.html')

    @app.route('/animalGuesser', methods=['GET'])
    def animal_guesser():
        animals = ["lion", "tiger", "elephant", "giraffe", "zebra", "panda", "koala"]
        random_animal = random.choice(animals)

        guess = request.args.get('guess', '').lower()

        if guess == random_animal:
            return jsonify({"result": "Correct! You guessed the animal!"}), 200
        elif guess:
            hint = f"The animal starts with '{random_animal[0]}'. Try again!"
            return jsonify({"result": "Incorrect guess", "hint": hint}), 200
        else:
            return jsonify({"animal": random_animal}), 200

    @app.route('/color', methods=['GET','POST'])
    def color_hexifier():
        color_name = request.args.get('color')
    
        print(f"Received color name: {color_name}")
    
        if color_name and color_name.lower() in matplotlib.colors.CSS4_COLORS:
            hex_code = matplotlib.colors.CSS4_COLORS[color_name.lower()]
            return f"The hex code for {color_name} is {hex_code}"
        else:
            return "Invalid color name"
        
    app.register_blueprint(dadjoke_bp)
        
    @app.route('/favoritequote', methods=['GET', 'POST'])
    def get_favorite_quote():
        favorite_quote = {
         "quote": "The only way to do great work is to love what you do.",
         "author": "Steve Jobs"
        }
        quotes = [favorite_quote]
        if request.method == 'GET':
            return jsonify(favorite_quote)  

        elif request.method == 'POST':
            new_quote = request.json 
            quotes.append(new_quote)  
            return jsonify({"message": "New favorite quote added!", "quote": new_quote}), 201
    
        elif request.method == 'PATCH':
        # Assuming the client sends the author's name to identify which quote to update
            author = request.json.get('author')
            updated_quote = request.json.get('quote')
        
        for quote in quotes:
            if quote['author'] == author:
                quote['quote'] = updated_quote
                return jsonify({"message": "Favorite quote updated!", "quote": quote}), 200
        
        return jsonify({"error": "Quote not found for the given author."}), 404

    @app.route('/fortune', methods=['GET'])
    def get_fortune():
        fortunes = [
            "You will find a fortune.",
            "A fresh start will put you on your way.",
            "Fortune favors the brave.",
            "Good news will come to you by mail.",
            "A beautiful, smart, and loving person will be coming into your life.",
            "A soft voice may be awfully persuasive.",
            "All your hard work will soon pay off."
        ]
        count = request.args.get('count', default=1, type=int)
        if count < 1:
            count = 1
        return jsonify({"fortunes": random.sample(fortunes, min(count, len(fortunes)))})
    
    @app.route('/fruitInfo', methods=['GET'])
    def fruit_info():
        fruits = {
            "apple": {"color": "red", "taste": "sweet"},
            "banana": {"color": "yellow", "taste": "sweet"},
            "lemon": {"color": "yellow", "taste": "sour"},
            "orange": {"color": "orange", "taste": "citrus"},
            "grape": {"color": "purple", "taste": "sweet"},
            "lime": {"color": "green", "taste": "sour"}
        }
    
        fruit_name = request.args.get('fruit')
    
        if fruit_name and fruit_name.lower() in fruits:
            info = fruits[fruit_name.lower()]
            return jsonify({
                "fruit": fruit_name,
                "color": info["color"],
                "taste": info["taste"]
            })
        else:
            return jsonify({"error": "Fruit not found. Please try apple, banana, lemon, orange, grape, or lime."}), 404
    
    @app.route('/items/<int:min_price>', methods=['GET'])
    def get_items(min_price):
        #min_price = request.args.get('min_price', default=0, type=int)
        items = load_items_from_file()
        filtered_items = [item for item in items if item['price'] >= min_price]
        #items = Item.query.filter(Item.price >= min_price).all()
        if not filtered_items:
            return jsonify({'message': 'No items found'}), 404
        return jsonify(filtered_items), 200

    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    @app.route('/weather/<city>', methods=['GET'])
    def weather(city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=imperial'
        response = requests.get(url)
        print("API Key:", WEATHER_API_KEY)
        print("Request URL:", url)
        #Returns error if invalid city is entered
        if response.status_code != 200:
            return render_template({"error": "City not found or API error."}), 404
        
        data = response.json()
        temperature = data['main']['temp']
        print(temperature)

        if temperature < 32:
            bg_color = "#56A5EC"
        elif 32 <= temperature < 50:
            bg_color = "#40E0D0"
        elif 50 <= temperature < 70:
            bg_color = "#50C878"
        elif 70 <= temperature < 80:
            bg_color = "#F5E216"
        elif 80 <= temperature < 90:
            bg_color = "#FFA500"
        elif 90 <= temperature < 100:
            bg_color = "#FF5F1F"
        else:
            bg_color = "#F62817"

            
        weather_data = {
            "city": city,
            "temperature": f"{data['main']['temp']}°F",
            "condition": data['weather'][0]['description'],
            "humidity": f"{data['main']['humidity']}%",
            "wind_speed": f"{data['wind']['speed']} mph",
            "bg_color": bg_color
        }
        return render_template('weather.html', weather=weather_data)
        

    @app.route('/howToMakeEndpoint', methods=['GET'])
    def get_endpoints():
        endpointSteps = [
            {"step 1": "Import Flask"},
            {"step 2": "Create app"},
            {"step 3": "Define endpoint with @app.route"},
            {"step 4": "Write the endpoint function"}
        ]
        step = request.args.get('step')
        if step and step.isdigit():
            step_num = int(step) - 1
            if 0 <= step_num < len(endpointSteps): 
             return jsonify(endpointSteps[step_num])
            return jsonify({"error": "Invalid step number"}), 400

        return jsonify(endpointSteps)

    app.register_blueprint(math_bp)
    app.register_blueprint(marathonFacts_bp)

    app.register_blueprint(mtg_bp)

    app.register_blueprint(motivation_bp)

    app.register_blueprint(photogallery_bp)

    app.register_blueprint(pizza_bp)

    @app.route('/pokefishing', methods=['GET','POST'])
    def fish():
        magikarp = [
            "a regular ol' Magikarp",
            "a calico pattern Magikarp",
            "a orange two-tone pattern Magikarp",
            "a pink dapple pattern Magikarp",
            "a gray diamond pattern Magikarp",
            "a purple patches pattern Magikarp",
            "a apricot tiger pattern Magikarp",
            "a brown stripes pattern Magikarp",
            "a orange forehead pattern Magikarp",
            "a blue raindrops pattern Magikarp",
            "a shiny Magikarp",
            "a... Oh no, it's a Gyarados!!",
            "a Goldeen and it's the biggest you've ever seen",
            "nothing... But you did see a Mudkip riding on a Lotad"
            ]
        success = random.choice([True, False])
        if success:
            caught = random.choice(magikarp)
        else:
            caught = "... Oops, you forgot to reel it in"
        return jsonify({"You caught": caught + "!"})

    @app.route('/randomFact', methods=['GET'])
    def random_fact():
        facts = [
            {"fact": "Honey never spoils."},
            {"fact": "Octopuses have three hearts."},
            {"fact": "Bananas are berries, but strawberries are not."},
            {"fact": "A day on Venus is longer than a year on Venus."},
            {"fact": "Sharks have been around longer than trees."},
            {"fact": "The ocean covers 71 percent of the Earth's surface and the average depth is 12,100 feet."}
        ]
        selected_show = random.choice(netflix_shows)
        return jsonify({"netflix_show": selected_show})

    @app.route('/multiply', methods=['GET'])
    def multiply():
        try:
            a = float(request.args.get('a'))
            b = float(request.args.get('b'))
            result = a * b
            return jsonify({'result': result}), 200
        except (TypeError, ValueError):
            return jsonify({'error': 'Invalid input'}), 400



    @app.route('/travel', methods=['GET','POST'])
    def travel():
        destinations = [
            {"You should go to": "Paris, France", "To fly from SLC it will take ": "9h 50m"},
            {"You should go to": "Rome, Italy", "To fly from SLC it will take ": "13hr 30m"},
            {"You should go to": "London, England", "To fly from SLC it will take ": "9hr 30m"},
            {"You should go to": "Tokyo, Japan", "To fly from SLC it will take ": "13hr 40m"},
            {"You should go to": "Barcelona, Spain", "To fly from SLC it will take ": "12hr 30m"},
            {"You should go to": "New York City, New York", "To fly from SLC it will take ": "4hr 35m"},
            {"You should go to": "Los Angeles, California", "To fly from SLC it will take ": "2hr"},
            {"You should go to": "Dublin, Ireland", "To fly from SLC it will take ": "11hr 30m"},
            {"You should go to": "Cairo, Egypt", "To fly from SLC it will take ": "15hr 15m"},
            {"You should go to": "Sydney, Australia", "To fly from SLC it will take ": "18hr 15m"},
            {"You should go to": "Sacramento, California", "To fly from SLC it will take ": "1hr 45m"},
            {"You should go to": "Salt Lake, Utah", "To fly from SLC it will take ": "You're already there silly"},
            {"You should go to": "Denver, Colorado", "To fly from SLC it will take ": "1hr 35m"},
            {"You should go to": "Santa Cruz, California", "To fly from SLC it will take ": "2hr"},
            ]
        
        picked = random.choice(destinations)
        return jsonify(picked)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

# we built this brick by brick and we will never stop