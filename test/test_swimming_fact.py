"""
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_swimming_fact(client):
    response = client.get('/swimming_fact')
    assert response.status_code == 200
    data = response.get_json()
    assert 'fact' in data
    assert data['fact'].startswith((
        'Swimming is', 
        'Michael Phelps', 
        'The front crawl', 
        'Humans have', 
        'Swimming burns'
    ))
    """