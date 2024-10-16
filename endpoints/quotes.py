from flask import Blueprint, jsonify, request
import random

quotes_bp = Blueprint('quotes', __name__)


@quotes_bp.route('/motivation', methods=['GET'])
def get_motivation():
    motivational_quotes = [
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Believe you can and you're halfway there.",
        "Act as if what you do makes a difference. It does.",
        "The harder you work for something, the greater you’ll feel when you achieve it."
    ]
    selected_quote = random.choice(motivational_quotes)
    return jsonify({"motivational_quote": selected_quote})
 
@quotes_bp.route('/quotes', methods=['GET'])
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
