
# Test to check the status code of /basketballFacts
def test_basketball_facts_status_code(client):
    response = client.get('/basketballFacts')
    assert response.status_code == 200

# Test to check the content type of the response from /basketballFacts
def test_basketball_facts_content_type(client):
    response = client.get('/basketballFacts')
    assert response.content_type == 'application/json'

# Test to check if the response contains a basketball fact
def test_basketball_facts_contains_fact(client):
    response = client.get('/basketballFacts')
    json_data = response.get_json()

    # Assert that the response is a dictionary
    assert isinstance(json_data, dict)

    # Assert that the response contains the 'basketball_fact' key
    assert 'basketball_fact' in json_data

    # Assert that the value of 'basketball_fact' is a string
    assert isinstance(json_data['basketball_fact'], str)