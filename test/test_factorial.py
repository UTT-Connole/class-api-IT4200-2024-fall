def test_factorial_single_positive(client):
    response = client.get('/factorial?n=5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 120

def test_factorial_single_zero(client):
    response = client.get('/factorial?n=0')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 1

def test_factorial_single_negative(client):
    response = client.get('/factorial?n=-5')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_factorial_multiple(client):
    response = client.get('/factorial?n=3&n=4&n=5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == [6, 24, 120]

def test_factorial_multiple_with_negative(client):
    response = client.get('/factorial?n=3&n=-4&n=5')
    assert response.status_code == 400
    assert b"No negative numbers:" in response.data

def test_noInput(client):
    response = client.get('/factorial')
    assert response.status_code == 400
    assert b"error" in response.data

def test_float(client):
    response = client.get('/factorial?n=5.5')
    assert response.status_code == 400
    assert b"error" in response.data
