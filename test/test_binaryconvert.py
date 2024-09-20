
def test_status_code(client):
    response = client.get('/convertToBinary?num=1')
    assert response.status_code == 200
    
def test_decimal(client):
    response = client.get('/convertToBinary?num=5')
    assert response.data.decode() == '101'

def test_zero(client):
    response = client.get('/convertToBinary?num=0')
    assert response.data.decode() == '0'

def test_negative(client):
    response = client.get('/convertToBinary?num=-1')
    assert response.data.decode() == 'Not compatable with negative input'

def test_float(client):
    response = client.get('/convertToBinary?num=1.1')
    assert response.data.decode() == 'Not compatable with float input'
