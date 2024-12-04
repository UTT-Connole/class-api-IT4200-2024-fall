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

@patch('endpoints.photogallery.render_template')
def test_photogallery_permissions(mock_render_template, client):
    mock_render_template.return_value = "Mocked template response"

    # Path to the image folder
    image_folder = os.path.join(client.application.root_path, 'images')

    # Check that the image folder exists and is readable
    assert os.path.exists(image_folder), "Image folder does not exist"
    assert os.access(image_folder, os.R_OK), "Image folder is not readable"

    # List image files
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Check that each image file is readable
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        assert os.path.isfile(image_path), f"{image_file} is not a file"
        assert os.access(image_path, os.R_OK), f"{image_file} is not readable"

    # Test the photogallery route
    response = client.get('/photogallery')
    assert response.status_code == 200
    assert b"Mocked template response" in response.data
