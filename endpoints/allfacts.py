from flask import Blueprint, jsonify, request
import random

allfacts_bp = Blueprint('allfacts', __name__)

facts = {
    "random": [
        "Honey never spoils.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries are not.",
        "A day on Venus is longer than a year on Venus.",
        "Sharks have been around longer than trees.",
        "The ocean covers 71 percent of the Earth's surface and the average depth is 12,100 feet."
    ],
    "swimming": [
        "Swimming is one of the best aerobic exercises.",
        "Michael Phelps holds the record for most Olympic gold medals at 23.",
        "The front crawl is the fastest swimming stroke.",
        "Humans have been swimming for thousands of years.",
        "Swimming burns more calories than running."
    ],
    "wrestling": [
        "Hulk Hogan won his first WWF Championship in 1984.",
        "The Undertaker has a 25-2 WrestleMania record.",
        "Stone Cold Steve Austin's 'Austin 3:16' speech revolutionized wrestling promos.",
        "Ric Flair is a 16-time world champion.",
        "Shawn Michaels is known as 'Mr. WrestleMania' for his outstanding performances on the big stage."
    ],
    "basketball": [
        "Michael Jordan has won six NBA championships.",
        "Kareem Abdul-Jabbar is the all-time leading scorer in NBA history.",
        "The NBA was founded in New York City on June 6, 1946.",
        "Wilt Chamberlain scored 100 points in a single game.",
        "The Boston Celtics have the most NBA titles with 17 championships.",
        "Basketball was invented in 1891 by Dr. James Naismith."
    ],
    "tennis": [
        "The fastest serve was 163.7 mph by Sam Groth.",
        "The longest match lasted 11 hours and 5 minutes.", 
        "Wimbledon is the oldest tournament.",
        "Yellow tennis balls were introduced in 1972.", 
        "Nadal has won the French Open 14 times."
    ],
    "history": [
        "The first modern Olympic Games were held in Athens in 1896."
    ],
    "popularity": [
        "The Super Bowl is the most-watched annual sporting event.",
        "Soccer is the most popular sport in the world."
    ],
    "studying": [
        "The Pomodoro Technique helps improve focus by working in 25-minute intervals.",
        "Exercise before studying can enhance learning and memory.",
        "Short, frequent study sessions are more effective than long, infrequent ones.",
        "Taking handwritten notes improves memory more than typing.",
        "Sleep plays a crucial role in memory consolidation after studying."
    ]
}

@allfacts_bp.route('/allFacts', methods=['GET'])
def all_facts():
    category = request.args.get('category', '').lower()

    if category in facts:
        fact = random.choice(facts[category])
        return jsonify({"category": category, "fact": fact})
    
    available_categories = list(facts.keys())
    message = f"Please choose a valid category. Available categories are: {', '.join(available_categories)}"
    return jsonify({"error": message})