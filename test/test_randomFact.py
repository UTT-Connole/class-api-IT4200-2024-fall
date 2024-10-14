"""
def test_randomFactStatus(client):
    response = client.get('/randomFact')
    assert response.status_code == 200

def test_randomFactJSONFormat(client):
    response = client.get('/randomFact')
    json_data = response.get_json()
    assert response.status_code == 200
    assert "fact" in json_data

def test_randomFactContent(client):
    response = client.get('/randomFact')
    assert response.status_code == 200
    json_data = response.get_json()
    predefined_facts = [
        "Honey never spoils.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries are not.",
        "A day on Venus is longer than a year on Venus.",
        "Sharks have been around longer than trees.",
        "The ocean covers 71 percent of the Earth's surface and the average depth is 12,100 feet."
    ]
    assert json_data['fact'] in predefined_facts

def test_randomFactTotalCount(client):
    response = client.get('/randomFact')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['totalFacts'] == 6 
"""