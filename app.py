from flask import Flask, request, jsonify, render_template
from binaryconvert import convertToBinary_bp
from endpoints.dadjoke import dadjoke_bp
from endpoints.brainrot import brainrot_bp
from endpoints.motivation import motivation_bp
import random
import matplotlib
#import requests   -App wont run with this not commented out.


def create_app():
    app = Flask(__name__)

    @app.route('/basketballFacts', methods=['GET'])
    def get_basketball_facts():
        basketball_facts = [
            "Michael Jordan has won six NBA championships.",
            "Kareem Abdul-Jabbar is the all-time leading scorer in NBA history.",
            "The NBA was founded in New York City on June 6, 1946.",
            "Wilt Chamberlain scored 100 points in a single game.",
            "The Boston Celtics have the most NBA titles with 17 championships."
        ]
        selected_fact = random.choice(basketball_facts)
        return jsonify({"basketball_fact": selected_fact})
    
    @app.route('/greet', methods=['GET'])
    def greet():
        return jsonify({"message": "Hello, Welcome to the API!"})

    @app.route('/greet/<name>', methods=['GET'])
    def greet_with_name(name):
        return jsonify({"message": f"Hello, {name}!"})
      
    @app.route('/')
    def hello_world():
        return "Hello World"
    
    app.register_blueprint(convertToBinary_bp)
    
    app.register_blueprint(dadjoke_bp)

    app.register_blueprint(brainrot_bp)

    app.register_blueprint(motivation_bp)

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
        {"author": "Marcus Aurelius", "quote": "Things are not asking to be judged by you."},
        {"author": "Marcus Aurelius", "quote": "The best revenge is to be unlike hom who performed the injury."},
        {"author": "Plato", "quote": "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light."},
        {"author": "Plato", "quote": "Wise men talk because they have something to say; fools, because they have to say something."},
        {"author": "Plato", "quote": "Human behavior flows from threee main sources: desire, emotion, and knowledge."},
        {"author": "Thorin Oakenshield", "quote": "If more of us valued food and cheer and song above hoarded gold, it would be a merrier world."}
        ]
        quote = random.choice(quotes)
        return jsonify(quote)

    @app.route('/calc', methods=['GET','POST'])
    def calc_main():
        x = request.args.get('x')
        y = request.args.get('y')
        op = request.args.get('op')
        
        if not (x and y and op):
            return "Invalid Input"
        
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return "Invalid Input"
        
        operations = {
            'add': x + y,
            'subtract': x - y,
            'multiply': x * y,
            'divide': x / y if y != 0 else "You cannot divide by 0"
        }
        
        result = operations.get(op, "You might have spelled something wrong or there is not the option. The current options are: add, subtract, multiply, divide")
        
        return str(result)
    
    @app.route('/twoManaCombos', methods=['GET'])
    def random_combo():
        two_m =[{ "name": "Azorius", "color_1": "white", "color_2": "blue"},
                { "name": "Boros", "color_1": "red", "color_2": "white"},
                { "name": "Dimir", "color_1": "blue", "color_2": "black"},
                { "name": "Golgari", "color_1": "black", "color_2": "green"},
                { "name": "Gruul", "color_1": "red", "color_2": "green"},
                { "name": "Izzet", "color_1": "blue", "color_2": "red"},
                { "name": "Orzhov", "color_1": "white", "color_2": "black"},
                { "name": "Rakdos", "color_1": "black", "color_2": "red"},
                { "name": "Selesnya", "color_1": "white", "color_2": "green"},
                { "name": "Simic", "color_1": "blue", "color_2": "black"}]
        color = request.args.get('color')
        if color:
            filtered_combos = [combo for combo in two_m if color.lower() in [combo['color_1'].lower(), combo['color_2'].lower()]]
            if not filtered_combos:
                return jsonify({"error": "No combinations found for the given color"}), 404
            
            r = random.choice(filtered_combos)
        else:
            r = random.choice(two_m)
        return jsonify(r)
    
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
    
    @app.route('/factorial', methods=['GET'])
    def factorial():
        n = request.args.get('n', type=int)
        if n is None:
            return "error", 400
        if n < 0:
            return "error", 400
        elif n == 0 or n == 1:
            return jsonify(result=1), 200
        else:
            result = 1
            for i in range (2, n + 1):
                result *= i
            return jsonify(result=result), 200
        
    @app.route('/power', methods=['GET'])
    def power():
        base = request.args.get('base', type=int)
        exp = request.args.get('exp', type=int)
        if base is None or exp is None:
            return "Invalid Input", 400
        result = base ** exp
        return jsonify(result=result), 200
        
    @app.route('/tennis_fact')
    def tennis_fact():
        tennis_facts = [
            {"fact": "The fastest serve was 163.7 mph by Sam Groth.", "category": "speed"},
            {"fact": "The longest match lasted 11 hours and 5 minutes.", "category": "record"},
            {"fact": "Wimbledon is the oldest tournament.", "category": "history"},
            {"fact": "Yellow tennis balls were introduced in 1972.", "category": "history"},
            {"fact": "Nadal has won the French Open 14 times.", "category": "achievement"}
        ]
        category = request.args.get('category')
        facts = [fact for fact in tennis_facts if fact['category'] == category] if category else tennis_facts
        if not facts:
            facts = tennis_facts
        return jsonify(random.choice(facts))
  
    @app.route('/sports_fact')
    def sports_fact():
        sports_facts = [
            "Basketball was invented in 1891 by Dr. James Naismith.",
            "The first modern Olympic Games were held in Athens in 1896.",
            "Soccer is the most popular sport in the world.",
            "Michael Phelps holds the record for the most Olympic gold medals.",
            "The Super Bowl is the most-watched annual sporting event."
        ]
        fact = random.choice(sports_facts)
        return jsonify({"fact": fact})

    @app.route('/pizzaToppings', methods=['GET'])
    def pizza_toppings():
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

        selected_crust = random.choice(crusts)
        selected_sauce = random.choice(sauces)  
        selected_toppings = random.sample(toppings, 3) 

        pizza = {
            "crust": selected_crust,
            "sauce": selected_sauce,
            "toppings": selected_toppings
        }

        return jsonify(pizza)

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
        return jsonify({"fortune": random.choice(fortunes)})
    
    @app.route('/color', methods=['GET','POST'])
    def color_hexifier():
        color_name = request.args.get('color')
    
        print(f"Received color name: {color_name}")
    
        if color_name and color_name.lower() in matplotlib.colors.CSS4_COLORS:
            hex_code = matplotlib.colors.CSS4_COLORS[color_name.lower()]
            return f"The hex code for {color_name} is {hex_code}"
        else:
            return "Invalid color name"
        
    WEATHER_API_KEY = 'a5b6f8eb1b20b57f80fa87f940e02857'
    @app.route('/weather/<city>', methods=['GET'])
    def weather(city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=imperial'
        response = requests.get(url)
        #Returns error if invalid city is entered
        if response.status_code != 200:
            return jsonify({"error": "City not found or API error."}), 404
        
        data = response.json()
        weather_data = {
            "temperature": f"{data['main']['temp']}°F",
            "condition": data['weather'][0]['description'],
            "humidity": f"{data['main']['humidity']}%",
            "wind_speed": f"{data['wind']['speed']} mph"
        }
        return jsonify(weather_data)

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
        caught = random.choice(magikarp)
        return jsonify({"You caught": caught + "!"})

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

    return app

app = create_app()

@app.route('/randomName', methods=['GET'])
def random_name():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    name = random.choice(names)
    return jsonify({"name": name})

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
    selected_fact = random.choice(facts)
    return jsonify(selected_fact)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/howToMakeEndpoint', methods=['GET'])
def get_endpoints():
	endpointSteps = [
		{"step 1":" Import Flask "},
		{"step 2":" Create app"},
		{"step 3":" Define endpoint with @app.route"},
		{"step 4":" write the endpoint function"}
    ]
	return jsonify("Follow these steps:"+ str(endpointSteps))

@app.route('/items', methods=['GET'])
def get_items():
    min_price = request.args.get('min_price', default=0, type=int)
    items = Item.query.filter(Item.price >= min_price).all()
    if not items:
        return jsonify({'message': 'No items found'}), 404
    return jsonify([item.serialize() for item in items]), 200

# we built this brick by brick and we will never stop