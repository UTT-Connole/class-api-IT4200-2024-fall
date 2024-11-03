import os
import subprocess
from flask import Blueprint, jsonify

version_bp = Blueprint('version', __name__)

@version_bp.route('/version', methods=['GET'])
def get_version():
    return jsonify({"version": get_repo_version()})

def get_repo_version():
    version = os.getenv('VERSION', 'DEV')
    return version