# test for 0
def test_zero(client):
    response = client.get('/factorial?n=0')
    assert response.status_code == 200
    assert b"1" in response.data

# test for 1
def test_one(client):
    response = client.get('/factorial?n=1')
    assert response.status_code == 200
    assert b"1" in response.data

# test a small number
def test_five(client):
    response = client.get('/factorial?n=5')
    assert response.status_code == 200
    assert b"120" in response.data

# test a big number
def test_ten(client):
    response = client.get('/factorial?n=10')
    assert response.status_code == 200
    assert b"3628800" in response.data

def test_negative(client):
    response = client.get('/factorial?n=-1')
    assert response.status_code == 400
    assert b"error" in response.data

def test_multipleNumbers(client):
    response = client.get('/factorial?n=5&n=3&n=2')
    assert response.status_code == 200
    assert b"120" in response.data
    assert b"6" in response.data
    assert b"2" in response.data

def test_multipleNegativeNumbers(client):
    response = client.get('/factorial?n=5&n=-1')
    assert response.status_code == 400
    assert b"error for -1" in response.data

def test_noInput(client):
    response = client.get('/factorial')
    assert response.status_code == 400
    assert b"error" in response.data