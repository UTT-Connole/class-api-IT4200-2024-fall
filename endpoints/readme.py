from flask import Flask, Blueprint, render_template_string
import markdown
import requests
import os
import subprocess
import threading

# Create a Blueprint for the welcome endpoint
readme_bp = Blueprint('readme', __name__)

GRIP_URL = 'http://localhost:6419'

def run_grip():
    """Function to run Grip as a subprocess."""
    subprocess.run(["grip", "README.md"])

# Start Grip in a separate thread
grip_thread = threading.Thread(target=run_grip, daemon=True)
grip_thread.start()

@readme_bp.route('/readme')
def readme():
    # Render the HTML content with a readme message and a link to the README.md served by Grip
    return render_template_string("""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>README</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body, html {
                height: 100%;
            }
            .centered {
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
        </style>
    </head>
    <body>
        <div class="container centered">
            <p class="text-center">
                <a href="{{ grip_url }}" target="_blank" class="btn btn-primary">View README.md</a>
            </p>
        </div>
    </body>
    </html>
    """, grip_url=GRIP_URL)