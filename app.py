from flask import Flask, request, jsonify, render_template, abort
from endpoints.readme import readme_bp
from endpoints.marathonfacts import marathonFacts_bp
from endpoints.dadjoke import dadjoke_bp
from endpoints.brainrot import brainrot_bp
from endpoints.motivation import motivation_bp
from endpoints.math import math_bp
from endpoints.mtg import mtg_bp
from endpoints.allfacts import allfacts_bp
from endpoints.pizza_meal import pizza_meal_bp
from endpoints.restaurants import restaurant_bp
from endpoints.soda import soda_bp
from endpoints.version import version_bp
from endpoints.quotes import quotes_bp
from endpoints.photogallery import photogallery_bp
from endpoints.pokefishing import pokefishing_bp
from endpoints.animalGuesser import animalGuess_bp
from endpoints.weather import weather_bp
from endpoints.fruitInfo import fruit_bp
from endpoints.name_generator import name_bp
from endpoints.color_hexifier import color_hexifier_bp
from endpoints.crypto import bitcoin_bp
from endpoints.fortune import fortune_bp
from endpoints.items import items_bp
import random, requests
import os, json
import time
from decimal import Decimal, getcontext 
import matplotlib, math

import boto3


def load_items_from_file():
    with open('items.json', 'r') as f:
        return json.load(f)
    
def create_app():
    app = Flask(__name__)
    automobiles = [{"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020}]
    app.register_blueprint(readme_bp)
    app.register_blueprint(brainrot_bp)
    app.register_blueprint(dadjoke_bp)
    app.register_blueprint(math_bp)
    app.register_blueprint(allfacts_bp)
    app.register_blueprint(marathonFacts_bp)
    app.register_blueprint(mtg_bp)
    app.register_blueprint(motivation_bp)
    app.register_blueprint(photogallery_bp)
    app.register_blueprint(pizza_meal_bp)
    app.register_blueprint(pokefishing_bp)
    app.register_blueprint(soda_bp)
    app.register_blueprint(version_bp)
    app.register_blueprint(quotes_bp)
    app.register_blueprint(animalGuess_bp)
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(weather_bp)
    app.register_blueprint(fruit_bp)
    app.register_blueprint(name_bp)
    app.register_blueprint(color_hexifier_bp)
    app.register_blueprint(fortune_bp)
    app.register_blueprint(bitcoin_bp, url_prefix='/api')
    app.register_blueprint(items_bp)


    @app.route('/crypto')
    def crypto_page():
        return render_template('crypto.html')

    @app.route('/db_test')
    def db_test():
        print("db_test")
        dynamo_url = os.environ.get('DYNAMO_URL') or 'http://localhost:8000'
        dynamo_region = os.environ.get('DYNAMO_REGION') or 'us-west-2'

        print('dynamo_url:', dynamo_url)
        print('dynamo_region:', dynamo_region)

        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamo_url, region_name=dynamo_region)
        table = dynamodb.Table('test')
        response = table.scan()
        return response['Items']

    continents = [
    {"id": 1, "name": "Africa", "area": 30370000, "population": 1340598000},
    {"id": 2, "name": "Antarctica", "area": 14000000, "population": 1106},
    {"id": 3, "name": "Asia", "area": 44579000, "population": 4641054775},
    {"id": 4, "name": "Europe", "area": 10180000, "population": 747636026},
    {"id": 5, "name": "North America", "area": 24709000, "population": 592072212},
    {"id": 6, "name": "Australia", "area": 8600000, "population": 42677813},
    {"id": 7, "name": "South America", "area": 17840000, "population": 430759766},
    ]

    @app.route('/continents', methods=['GET'])
    def get_continents():
        """Return a list of all continents."""
        return jsonify(continents)

    @app.route('/continents/<int:continent_id>', methods=['GET'])
    def get_continent(continent_id):
        """Return details of a single continent by its ID."""
        continent = next((cont for cont in continents if cont["id"] == continent_id), None)
        if continent:
            return jsonify(continent)
        else:
            # Use abort to return a 404 response
            abort(404, description="Continent not found")
    
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
        
    @app.route('/automobiles', methods=['GET', 'POST'])
    def handle_automobiles():
        if request.method == 'POST':
            new_auto = request.json
            new_auto['id'] = automobiles[-1]['id'] + 1 if automobiles else 1
            automobiles.append(new_auto)
            return jsonify(new_auto), 201
        return jsonify(automobiles), 200

    @app.route('/automobiles/<int:automobile_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_automobile(automobile_id):
        automobile = next((auto for auto in automobiles if auto['id'] == automobile_id), None)
        if not automobile:
            return jsonify({"error": "Automobile not found"}), 404
        if request.method == 'PUT':
            automobile.update(request.json)
            return jsonify(automobile), 200
        elif request.method == 'DELETE':
            automobiles.remove(automobile)
            return jsonify({"message": "Automobile deleted"}), 200
        return jsonify(automobile), 200

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

    @app.route('/netflix-shows', methods=['GET'])
    def get_netflix_shows():
        title_filter = request.args.get('title')
        netflix_shows = [
            {"title": "Stranger Things", "fact": "The Demogorgon suit was mostly practical effects."},
            {"title": "The Witcher", "fact": "Henry Cavill performed many of his own stunts."},
            {"title": "Money Heist", "fact": "The show was initially a flop in Spain before Netflix acquired it."},
            {"title": "The Crown", "fact": "Claire Foy was paid less than Matt Smith despite being the lead."},
            {"title": "Narcos", "fact": "The show initially faced criticism for its portrayal of Colombian culture."},
            {"title": "BoJack Horseman", "fact": "The show used celebrity guest stars who played exaggerated versions of themselves."},
            {"title": "Black Mirror", "fact": "The show explores the dark side of technology and modern society."}
        ]

        if title_filter:
                filtered_shows = [show for show in netflix_shows if title_filter.lower() in show["title"].lower()]
                if not filtered_shows:
                    return jsonify({"error": "No shows found with the specified title."}), 404
                selected_show = random.choice(filtered_shows)
        else:
            selected_show = random.choice(netflix_shows)
            
        return jsonify({"netflix_show": selected_show})

    @app.route('/multiply', methods=['GET'])
    def multiply():
        try:
            # Get the 'numbers' parameter and split it into a list of numbers
            numbers = request.args.get('numbers')
            if not numbers:
                return jsonify({'error': 'No input provided'}), 400
        
            # Convert the list of string numbers to floats
            number_list = [float(num) for num in numbers.split(',')]
            result = 1
            for num in number_list:
                result *= num
            
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
            
        max_duration = request.args.get('max_duration')
    
        if max_duration:
            max_hours = int(max_duration)
            # Filter destinations to those with flight time within max_duration
            destinations = [d for d in destinations if 'hr' in d["To fly from SLC it will take "] and int(d["To fly from SLC it will take "].split('hr')[0]) <= max_hours]
    
        picked = random.choice(destinations) if destinations else {"message": "No destinations within specified duration."}
        return jsonify(picked)
    
    @app.route('/xkcd-comic', methods=['GET'])
    def get_random_xkcd_comic():
        random_comic_num = random.randint(1, 2450)
        url = f"http://xkcd.com/{random_comic_num}/info.0.json"
        response = requests.get(url)

        if response.status_code != 200:
            return render_template('xkcd_comic.html', error="Comic not found"), 404
        
        comic_data = response.json()
        return render_template('xkcd_comic.html', comic=comic_data)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

# we built this brick by brick and we will never stop