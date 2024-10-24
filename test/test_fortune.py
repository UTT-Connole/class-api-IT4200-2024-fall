import pytest, app

def test_status(client):
    response = client.get('/fortune')
    assert response.status_code == 200

def test_contains_fortunes_key(client):
    response = client.get('/fortune')
    json_data = response.get_json()
    assert "fortunes" in json_data

def test_single_fortune(client):
    response = client.get('/fortune')
    json_data = response.get_json()
    assert len(json_data["fortunes"]) == 1

def test_multiple_fortunes(client):
    response = client.get('/fortune?count=3')
    json_data = response.get_json()
    assert len(json_data["fortunes"]) == 3

def test_valid_fortunes(client):
    response = client.get('/fortune?count=5')
    json_data = response.get_json()
    valid_fortunes = [
        "You will find a fortune.",
        "A fresh start will put you on your way.",
        "Fortune favors the brave.",
        "Good news will come to you by mail.",
        "A beautiful, smart, and loving person will be coming into your life.",
        "A soft voice may be awfully persuasive.",
        "All your hard work will soon pay off."
    ]
    for fortune in json_data["fortunes"]:
        assert fortune in valid_fortunes

def test_invalid_count(client):
    response = client.get('/fortune?count=0')
    json_data = response.get_json()
    assert len(json_data["fortunes"]) == 1
