import os
import subprocess
from flask import Blueprint, jsonify

version_bp = Blueprint('version', __name__)

@version_bp.route('/version', methods=['GET'])
def get_version():
    """
    Returns the version of the app.
    >>> app.test_client().get('/version').status_code
    200
    >>> app.test_client().get('/version').json['version']
    'DEV'
    """
    return jsonify({"version": get_repo_version()})

def get_repo_version():
    """
    Returns the repo version or 'DEV' if the environment variable isn't set.
    
    >>> get_repo_version()
    'DEV'
    """
    version = os.getenv('VERSION', 'DEV')
    return version