
def test_status_code(client):
    response = client.get('/convertToBinary?num=1&type=decimal')
    assert response.status_code == 200
    
def test_decimal(client):
    response = client.get('/convertToBinary?num=5&type=decimal')
    assert response.data.decode() == '101'

def test_binary(client):
    response = client.get('/convertToBinary?num=101&type=binary')
    assert response.data.decode() == '5'

def test_decimal_zero(client):
    response = client.get('/convertToBinary?num=0&type=decimal')
    assert response.data.decode() == '0'

def test_binary_zero(client):
    response = client.get('/convertToBinary?num=0&type=binary')
    assert response.data.decode() == '0'

def test_decimal_negative(client):
    response = client.get('/convertToBinary?num=-1&type=decimal')
    assert response.data.decode() == 'Not compatible with negative input'

def test_binary_negative(client):
    response = client.get('/convertToBinary?num=-101&type=binary')
    assert response.data.decode() == 'Not compatible with negative input'

def test_decimal_float(client):
    response = client.get('/convertToBinary?num=1.1&type=decimal')
    assert response.data.decode() == 'Not compatible with float input'

def test_binary_float(client):
    response = client.get('/convertToBinary?num=101.1&type=binary')
    assert response.data.decode() == 'Not compatible with float input'

def test_decimal_str(client):
    response = client.get('/convertToBinary?num=abc&type=decimal')
    assert response.data.decode() == 'Please input a valid number'

def test_binary_str(client):
    response = client.get('/convertToBinary?num=abc&type=binary')
    assert response.data.decode() == 'Please input a valid number'

def test_decimal_blank(client):
    response = client.get('/convertToBinary?num=&type=decimal')
    assert response.data.decode() == 'Please input a valid number'

def test_binary_blank(client):
    response = client.get('/convertToBinary?num=&type=binary')
    assert response.data.decode() == 'Please input a valid number'

def test_type_blank(client):
    response = client.get('/convertToBinary?num=101&type=')
    assert response.data.decode() == 'Invalid Type. Please use [decimal] for Decimal to Binary converstions and [binary] for Binary to Decimal converstions'
