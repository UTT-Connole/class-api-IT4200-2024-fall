import random
from flask import Blueprint, render_template

# Create a blueprint for dadjoke
dadjoke_bp = Blueprint('dadjoke', __name__)

@dadjoke_bp.route('/dadjoke', methods=['GET'])
def dad_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I would avoid the sushi if I was you. It's a little fishy.",
        "Today, my son asked 'Can I have a bookmark?' and I burst into tears. 11 years old and he still doesn't know my name is Brian.",
        "I went to the aquarium this weekend, but I didn't stay long. There's something fishy about that place.",
        "I gave my handyman a to-do list, but he only did jobs 1, 3, and 5. Turns out he only does odd jobs.",
        "I'm reading a horror story in braille. Something bad is going to happen, I can just feel it."
    ]
    
    # Choose a random joke
    joke = random.choice(jokes)
    
    # Pass the joke to the HTML template
    return render_template('dadjoke.html', joke=joke)
