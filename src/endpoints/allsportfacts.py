from flask import Blueprint, jsonify, request
import random

allsportfacts_bp = Blueprint('allsportfacts', __name__)

@allsportfacts_bp.route('/tennis_fact')
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
  
@allsportfacts_bp.route('/sports_fact')
def sports_fact():
    sports_facts = [
        {"fact": "Basketball was invented in 1891 by Dr. James Naismith.", "category": "history"},
        {"fact": "The first modern Olympic Games were held in Athens in 1896.", "category": "history"},
        {"fact": "Soccer is the most popular sport in the world.", "category": "popularity"},
        {"fact": "Michael Phelps holds the record for the most Olympic gold medals.", "category": "achievement"},
        {"fact": "The Super Bowl is the most-watched annual sporting event.", "category": "popularity"}
    ]
    category = request.args.get('category')
    facts = [fact for fact in sports_facts if fact['category'] == category] if category else sports_facts
    if not facts:
        facts = sports_facts
    return jsonify(random.choice(facts))

@allsportfacts_bp.route('/basketballFacts', methods=['GET'])
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
