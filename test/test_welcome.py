import pytest
from flask import Flask
from endpoints.welcome import welcome_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(welcome_bp)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_welcome_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the IT4200 class API!' in response.data
    assert b'View README.md' in response.data

def test_grip_url(client):
    response = client.get('/')
    assert response.status_code == 200
    # Check if the Grip URL is included in the rendered HTML
    assert b'http://localhost:6419' in response.data

def test_response_content_type(client):
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'

# Additional tests can be added as needed
