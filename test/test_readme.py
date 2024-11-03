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
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_readme_endpoint_html_structure(client):
    """Test that the /readme endpoint renders HTML content."""
    response = client.get('/readme')
    html = response.get_data(as_text=True)
    
    assert '<!doctype html>' in html, "Expected HTML doctype in response"
    assert '<title>README</title>' in html, "Expected title 'README' in response"
    assert '<div' in html, "Expected HTML div tags in response for README content structure"

def test_readme_endpoint_contains_readme_content(client):
    """Test that the /readme endpoint includes unique content from README.md."""
    response = client.get('/readme')
    html = response.get_data(as_text=True)
    
    # Check for general README markdown elements rendered by grip, such as headers or sections
    assert "Welcome" in html or "##" in html, "Expected content from README.md in rendered HTML"
