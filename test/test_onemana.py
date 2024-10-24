import pytest, app

def test_status(client):
    response = client.get('/MTGmana')
    assert response.status_code == 200

def test_correct_output(client):
    response = client.get('/MTGmana')
    print(response)
    json_data = response.get_json()
    assert json_data is not None
    assert isinstance(json_data, dict)
    assert len(json_data) == 2

def test_contains_keys(client):
    response = client.get('/MTGmana')
    json_data = response.get_json()
    assert "Color" in json_data
    assert "Known for" in json_data

def test_valid_color(client):
    response = client.get('/MTGmana')
    json_data = response.get_json()
    valid_colors = ["white", "blue", "black", "red", "green"]
    assert json_data["Color"] in valid_colors

def test_known_for_correctness(client):
    response = client.get('/MTGmana')
    json_data = response.get_json()
    color_traits = {
        "white": "order and protection",
        "blue": "knowledge and control",
        "black": "power and corruption",
        "red": "chaos and passion",
        "green": "growth and nature"
    }
    assert json_data["Known for"] == color_traits[json_data["Color"]]
