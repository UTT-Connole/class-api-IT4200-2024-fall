import os
from flask import Blueprint, jsonify, send_from_directory, current_app, render_template

# Define the blueprint for photogallery
photogallery_bp = Blueprint('photogallery', __name__)

@photogallery_bp.route('/photogallery', methods=['GET'])
def photogallery():
    # Directory where images are stored
    image_folder = os.path.join(current_app.root_path, 'images')

    # Get list of image filenames in the folder
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Render template to display images
    return render_template('photogallery.html', images=image_files)

@photogallery_bp.route('/images/<filename>', methods=['GET'])
def serve_image(filename):
    # Serve an image from the images folder
    image_folder = os.path.join(current_app.root_path, 'images')
    return send_from_directory(image_folder, filename)
