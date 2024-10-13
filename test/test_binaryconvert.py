import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_status_code(client):
    response = client.get('/calc?x=5&y=&op=decimal')
    assert response.status_code == 200

def test_decimal(client):
    response = client.get('/calc?x=5&y=&op=decimal')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == '101'

def test_binary(client):
    response = client.get('/calc?x=101&y=&op=binary')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == '5'

def test_decimal_zero(client):
    response = client.get('/calc?x=0&y=&op=decimal')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == '0'

def test_binary_zero(client):
    response = client.get('/calc?x=0&y=&op=binary')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == '0'

def test_decimal_negative(client):
    response = client.get('/calc?x=-1&y=&op=decimal')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 'Not compatible with negative input'

def test_binary_negative(client):
    response = client.get('/calc?x=-1&y=&op=binary')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == 'Not compatible format to convert to binary'

def test_decimal_float(client):
    response = client.get('/calc?x=5.5&y=&op=decimal')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == 'Invalid Input'

def test_binary_float(client):
    response = client.get('/calc?x=5.5&y=&op=binary')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == 'Invalid Input'

def test_decimal_str(client):
    response = client.get('/calc?x=abc&y=&op=decimal')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == 'Invalid Input'

def test_binary_str(client):
    response = client.get('/calc?x=abc&y=&op=binary')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == 'Invalid Input'

def test_decimal_blank(client):
    response = client.get('/calc?x=&y=&op=decimal')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == '0'

def test_binary_blank(client):
    response = client.get('/calc?x=&y=&op=binary')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == '0'