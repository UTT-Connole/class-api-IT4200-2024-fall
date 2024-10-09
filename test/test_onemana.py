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