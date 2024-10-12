
def test_status_code(client):
    response = client.get('/calc?x=5&y=&op=decimal')
    assert response.status_code == 200
    
def test_decimal(client):
    response = client.get('/calc?x=5&y=&op=decimal')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '101' in html_data

def test_binary(client):
    response = client.get('/calc?x=101&y=&op=binary')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '5' in html_data

def test_decimal_zero(client):
    response = client.get('/calc?x=0&y=&op=decimal')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '0' in html_data

def test_binary_zero(client):
    response = client.get('/calc?x=0&y=&op=binary')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '0' in html_data

def test_decimal_negative(client):
    response = client.get('/calc?x=-1&y=&op=decimal')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert 'Not compatible with negative input' in html_data

def test_binary_negative(client):
    response = client.get('/calc?x=-1&y=&op=binary')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert 'Not compatible format to convert to binary' in html_data

def test_decimal_float(client):
    response = client.get('/calc?x=5.5&y=&op=decimal')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert 'Invalid Input' in html_data

def test_binary_float(client):
    response = client.get('/calc?x=5.5&y=&op=binary')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert 'Invalid Input' in html_data

def test_decimal_str(client):
    response = client.get('/calc?x=abc&y=&op=decimal')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert 'Invalid Input' in html_data

def test_binary_str(client):
    response = client.get('/calc?x=abc&y=&op=binary')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert 'Invalid Input' in html_data

def test_decimal_blank(client):
    response = client.get('/calc?x=&y=&op=decimal')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '0' in html_data

def test_binary_blank(client):
    response = client.get('/calc?x=&y=&op=binary')
    assert response.status_code == 200
    html_data = response.get_data(as_text=True)
    assert '0' in html_data
