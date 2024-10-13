def test_response(client):
    response = client.get('/pokefishing')
    assert isinstance(response.json, dict), "Response should be a dictionary."
    assert "You caught" in response.json, "Response should contain 'You caught' key."
    assert response.status_code == 200

def test_structure(client):
    response = client.get('/pokefishing')
    json_data = response.json
    assert isinstance(json_data, dict), "The response should be a dictionary."
    assert len(json_data) == 1, "The response should have exactly one key."
    assert "You caught" in json_data, "The response should have the key 'You caught'."

def test_nonEmptyResponse(client):
    response = client.get('/pokefishing')
    catch = response.json["You caught"]
    assert catch.strip() != "", "The 'You caught' value should not be empty."
