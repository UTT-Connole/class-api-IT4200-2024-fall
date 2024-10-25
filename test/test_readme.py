import pytest
from flask import Flask
from endpoints.readme import readme_bp

@pytest.fixture
def client():
    # Create a Flask app instance and register the readme blueprint
    app = Flask(__name__)
    app.register_blueprint(readme_bp)

    # Use the app to create a test client
    with app.test_client() as client:
        yield client

def test_readme_endpoint_status_code(client):
    """Test that the /readme endpoint returns a 200 status code."""
    response = client.get('/readme')
    assert response.status_code == 200, "Expected status code 200, but got {response.status_code}"

def test_readme_endpoint_content(client):
    """Test that the /readme endpoint returns HTML with the README link."""
    response = client.get('/readme')
    html = response.get_data(as_text=True)
    
    assert '<!doctype html>' in html, "Expected HTML doctype in response"
    assert '<title>README</title>' in html, "Expected title 'README' in response"
    assert 'View README.md' in html, "Expected button text 'View README.md' in response"
    assert 'href="http://localhost:6419"' in html, "Expected link to Grip server at http://localhost:6419"

def test_readme_endpoint_grip_url(client):
    """Test that the /readme endpoint correctly includes the GRIP_URL link."""
    response = client.get('/readme')
    html = response.get_data(as_text=True)
    
    grip_url = 'http://localhost:6419'
    assert grip_url in html, f"Expected grip_url '{grip_url}' in the rendered HTML"
