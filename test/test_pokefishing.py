def test_response(client):
    response = client.get('/pokefishing')
    assert isinstance(response.json, dict), "Response should be a dictionary."
    assert "message" in response.json, "Response should contain 'message' key."
    assert response.status_code == 200

def test_structure(client):
    response = client.get('/pokefishing')
    json_data = response.json
    assert isinstance(json_data, dict), "The response should be a dictionary."
    assert len(json_data) == 1, "The response should have exactly one key."
    assert "message" in json_data, "The response should have the key 'message'."

def test_nonEmptyResponse(client):
    response = client.get('/pokefishing')
    message = response.json["message"]
    assert message.strip() != "", "The 'message' value should not be empty."
