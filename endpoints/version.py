from flask import Blueprint, jsonify
import subprocess

version_bp = Blueprint('version', __name__)xxxx

@version_bp.route('/version', methods=['GET'])
def get_version():
    try:
        # Get the latest tag commit
        latest_tag_commit = subprocess.check_output(["git", "rev-list", "--tags", "--max-count=1"]).strip().decode('utf-8')
        # Get the tag name from the commit
        version = subprocess.check_output(["git", "describe", "--tags", latest_tag_commit]).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        version = 'DEV'
    return jsonify({"version": version})