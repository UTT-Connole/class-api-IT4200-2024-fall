import pytest, app

def test_status(client):
    response = client.get('/twoManaCombos')
    assert response.status_code == 200

def test_correct_output(client):
    response = client.get('/twoManaCombos')
    print(response)
    json_data = response.get_json()
    assert json_data is not None
    assert isinstance(json_data, dict)
    assert len(json_data) == 3

def test_invalid_color(client):
    test_color = 'purple'
    response = client.get(f'/twoManaCombos?color={test_color}')
    assert response.status_code == 404
    json_data = response.get_json()
    assert 'error' in json_data
    assert json_data['error'] == 'No combinations found for the given color'