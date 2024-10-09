def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_wrestling_fact(client):
    response = client.get('/wrestling_fact')
    assert response.status_code == 200
    data = response.get_json()
    assert 'fact' in data
    assert data['fact'].startswith((
        'Hulk Hogan', 
        'The Undertaker', 
        'Stone Cold Steve Austin', 
        'Ric Flair', 
        'Shawn Michaels'
    ))