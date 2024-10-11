from flask import Blueprint
import random

# Create a blueprint for marathonFacts
marathonFacts_bp = Blueprint('marathonFacts', __name__)

@marathonFacts_bp.route('/marathonFacts', methods=['GET'])
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
    return "Category: " + random_fact["category"] + "<br><br>" + "Fact: " + random_fact["fact"]