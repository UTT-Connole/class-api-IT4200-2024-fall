def test_randomFactStatus(client):
    response = client.get('/allFacts')
    assert response.status_code == 200

def test_validCategoryWrestling(client):
    response = client.get('/allFacts?category=wrestling')
    assert response.status_code == 200
    data = response.get_json()
    assert data['category'] == 'wrestling'
    assert data['fact'] in facts['wrestling']

def test_validCategoryStudying(client):
    response = client.get('/allFacts?category=studying')
    assert response.status_code == 200

def test_validCategorySwimming(client):
    response = client.get('/allFacts?category=swimming')
    assert response.status_code == 200
    data = response.get_json()
    assert data['category'] == 'swimming'
    assert data['fact'] in facts['swimming']

def test_validCategoryBasketball(client):
    response = client.get('/allFacts?category=basketball')
    assert response.status_code == 200

def test_validCategoryTennis(client):
    response = client.get('/allFacts?category=tennis')
    assert response.status_code == 200
    data = response.get_json()
    assert data['category'] == 'tennis'
    assert data['fact'] in facts['tennis']

def test_invalidCategory(client):
    response = client.get('/allFacts?category=invalid')
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    assert "Please choose a valid category." in data['error']

def test_categoriesListInErrorResponse(client):
    response = client.get('/allFacts?category=invalid')
    data = response.get_json()
    assert "Available categories are:" in data['error']
    assert any(category in data['error'] for category in facts.keys())  

def test_multipleRequestsDifferentCategories(client):
    response1 = client.get('/allFacts?category=swimming')
    response2 = client.get('/allFacts?category=wrestling')
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response1.get_json()['category'] == 'swimming'
    assert response2.get_json()['category'] == 'wrestling'

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
