def test_allZero(client):
    response = client.get('/power?base=0&exp=0')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == "1.000000"
    assert data['base'] == 0
    assert data['exponent'] == 0

def test_zeroBase(client):
    response = client.get('/power?base=0&exp=1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == "0.000000"

def test_zeroExp(client):
    response = client.get('/power?base=348&exp=0')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == "1.000000"

def test_normal(client):
    response = client.get('/power?base=9&exp=2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == "81.000000"

def test_negativeBase(client):
    response = client.get('/power?base=-5&exp=2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == "25.000000"

def test_negativeExp(client):
    response = client.get('/power?base=5&exp=-2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == "0.040000"

def test_negativeBoth(client):
    response = client.get('/power?base=-5&exp=-2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == "0.040000"

def test_negativeBasePositiveExp(client):
    response = client.get('/power?base=-2&exp=2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == "4.000000"

def test_zeroBaseNegativeExp(client):
    response = client.get('/power?base=0&exp=-2')
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == "Cannot raise 0 to a negative power"

# New test cases for enhanced functionality
def test_multiple_bases(client):
    response = client.get('/power?base=2,3,4&exp=2')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['calculations']) == 3
    assert data['calculations'][0]['result'] == "4.000000"
    assert data['calculations'][1]['result'] == "9.000000"
    assert data['calculations'][2]['result'] == "16.000000"

def test_scientific_notation(client):
    response = client.get('/power?base=2&exp=10&notation=scientific')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == "1.024000e+03"
    assert data['notation'] == "scientific"

def test_custom_precision(client):
    response = client.get('/power?base=2&exp=0.5&precision=3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == "1.414"

def test_invalid_precision(client):
    response = client.get('/power?base=2&exp=2&precision=21')
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == "Precision must be between 0 and 20"

def test_negative_base_fractional_exp(client):
    response = client.get('/power?base=-4&exp=0.5')
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == "Cannot raise negative numbers to fractional powers"

def test_invalid_base_format(client):
    response = client.get('/power?base=invalid&exp=2')
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == "Invalid base value(s)"

def test_multiple_bases_with_scientific_notation(client):
    response = client.get('/power?base=2,3,4&exp=3&notation=scientific')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['calculations']) == 3
    assert data['calculations'][0]['result'] == "8.000000e+00"
    assert data['calculations'][1]['result'] == "2.700000e+01"
    assert data['calculations'][2]['result'] == "6.400000e+01"