def test_randomFactStatus(client):
    response = client.get('/allFacts')
    assert response.status_code == 200

def test_randomFactJSONFormat(client):
    response = client.get('/allFacts')
    json_data = response.get_json()
    assert response.status_code == 200
    assert "fact" in json_data

def test_random_fact(client):
    response = client.get('/allFacts?category=random')
    assert response.status_code == 200
    json_data = response.get_json()
    facts_response = client.get('/facts')
    facts_data = facts_response.get_json()
    predefined_facts = facts_data['random']
    assert json_data["fact"] in predefined_facts

def test_wrestling_fact(client):
    response = client.get('/allFacts?category=wrestling')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'fact' in json_data
    facts_response = client.get('/facts')
    facts_data = facts_response.get_json()
    predefined_facts = facts_data['wrestling']
    assert json_data["fact"] in predefined_facts

def test_swimming_fact(client):
    response = client.get('/allFacts?category=swimming')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'fact' in json_data
    facts_response = client.get('/facts')
    facts_data = facts_response.get_json()
    predefined_facts = facts_data['swimming']
    assert json_data["fact"] in predefined_facts

def test_basketball_fact(client):
    response = client.get('/allFacts?category=basketball')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'fact' in json_data
    facts_response = client.get('/facts')
    facts_data = facts_response.get_json()
    predefined_facts = facts_data['basketball']
    assert json_data["fact"] in predefined_facts