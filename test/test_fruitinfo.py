import json

def test_post_new_fruit(client):
    response = client.post('/fruitInfo?fruit=plum&color=purple&taste=sweet')
    data = json.loads(response.data)
    assert 'message' in data
    assert data['message'] == 'plum added successfully!'

def test_post_fruit_missing_data(client):
    response = client.post('/fruitInfo?fruit=&color=yellow&taste=sour')
    data = json.loads(response.data)
    assert 'error' in data

def test_post_fruit_incomplete_data(client):
    response = client.post('/fruitInfo?fruit=cherry&color=red')
    data = json.loads(response.data)
    assert 'error' in data

def test_get_all_fruits(client):
    response = client.get('/fruitInfo')
    data = json.loads(response.data)
    assert data
    assert 'plum' in data