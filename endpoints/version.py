from flask import Blueprint, jsonify
import subprocess

version_bp = Blueprint('version', __name__)

@version_bp.route('/version', methods=['GET'])
def get_version():
    return jsonify({"version": get_repo_version()})

@version_bp.route('/current-version', methods=['GET'])
def get_current_version():
    return jsonify({"version": get_working_version()})

def get_repo_version():
    try:
        # Get the latest tag commit
        latest_tag_commit = subprocess.check_output(["git", "rev-list", "--tags", "--max-count=1"]).strip().decode('utf-8')
        # Get the tag name from the commit
        version = subprocess.check_output(["git", "describe", "--tags", latest_tag_commit]).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        version = 'DEV'
    return version

def get_working_version():
    try:
        # Get the current commit hash
        current_commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode('utf-8')
        # Get the tag name from the current commit, if it exists
        version = subprocess.check_output(["git", "describe", "--tags", current_commit]).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        version = 'DEV'
    return version