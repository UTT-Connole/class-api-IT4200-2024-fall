from flask import Flask, render_template
import os
import pytest
from endpoints.photogallery import photogallery_bp
from unittest.mock import patch

@pytest.fixture
def client():
    # Create a temporary Flask app for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(photogallery_bp)
    
    # Ensure that the image folder exists during tests
    test_image_folder = os.path.join(app.root_path, 'images')
    os.makedirs(test_image_folder, exist_ok=True)

    with app.test_client() as client:
        yield client

@patch('endpoints.photogallery.render_template')
def test_photogallery(mock_render_template, client):
    # Mock the rendering of the template to bypass actual HTML loading
    mock_render_template.return_value = "Mocked template response"

    # Test if photogallery route returns a valid response
    response = client.get('/photogallery')
    assert response.status_code == 200
    assert b"Mocked template response" in response.data
