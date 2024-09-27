def test_allZero(client):
    response = client.get('/power?base=0&exp=0')
    assert response.status_code == 200
    assert b"1" in response.data

def test_zeroBase(client):
    response = client.get('/power?base=0&exp=1')
    assert response.status_code == 200
    assert b"0" in response.data

def test_zeroExp(client):
    response = client.get('/power?base=348&exp=0')
    assert response.status_code == 200
    assert b"1" in response.data

def test_normal(client):
    response = client.get('/power?base=9&exp=2')
    assert response.status_code == 200
    assert b"81" in response.data

def test_negativeBase(client):
    response = client.get('/power?base=-5&exp=2')
    assert response.status_code == 200
    assert b"25" in response.data