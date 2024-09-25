# test for 0
def test_zero(client):
    response = client.get('/factorial?n=0')
    assert response.status_code == 200
  
# test for 1
def test_one(client):
    response = client.get('/factorial?n=1')
    assert response.status_code == 200

# test a small number
def test_five(client):
    response = client.get('/factorial?n=5')
    assert response.status_code == 200

# test a big number
def test_ten(client):
    response = client.get('/factorial?n=10')
    assert response.status_code == 200

def test_negative(client):
    response = client.get('/factorial?n=-1')
    assert response.status_code == 400