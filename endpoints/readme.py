import os
import subprocess
import threading
from flask import Blueprint, render_template_string
import requests

# Define the blueprint for the readme endpoint
readme_bp = Blueprint('readme', __name__)

# Grip server URL
GRIP_URL = 'http://localhost:6419'

def run_grip():
    """Function to run Grip as a subprocess."""
    subprocess.run(["grip", "README.md"])

# Start Grip in a separate thread if it's not already running
grip_thread = threading.Thread(target=run_grip, daemon=True)
grip_thread.start()

@readme_bp.route('/readme', methods=['GET'])
def readme():
    # Fetch the rendered README content from Grip
    try:
        response = requests.get(f"{GRIP_URL}/README.md")
        if response.status_code == 200:
            readme_content = response.text
        else:
            readme_content = "<p>Error loading README content.</p>"
    except requests.exceptions.RequestException:
        readme_content = "<p>Could not connect to Grip server.</p>"

    # Render the README content inline on the page
    return render_template_string("""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>README</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container my-4">
            <h1 class="text-center">Welcome to the README</h1>
            <div class="content">
                {{ readme_content|safe }}
            </div>
        </div>
    </body>
    </html>
    """, readme_content=readme_content)
