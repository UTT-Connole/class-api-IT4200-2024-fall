
def test_zero(client):
    response = client.get('/factorial')
    assert response.status_code == 200

def test_fail(client):
    assert False

def test_True(client):
    assert True