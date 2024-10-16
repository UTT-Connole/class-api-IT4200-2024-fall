def test_get_study_facts(client):
    # Send a GET request to /study-facts
    response = client.get('/study-facts')  
    assert response.status_code == 200  # Assert that the response status is 200 (OK)
    assert b"study_fact" in response.data  # Ensure "study_fact" is in the returned data
