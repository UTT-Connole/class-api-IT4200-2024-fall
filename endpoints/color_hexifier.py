from flask import Blueprint, render_template, request
import matplotlib

color_hexifier_bp = Blueprint('color_hexifier', __name__)

@color_hexifier_bp.route('/color', methods=['GET'])
def color_hexifier():
    return render_template('color_hexifier.html')

@color_hexifier_bp.route('/get_color_hex', methods=['GET'])
def get_color_hex():
    color_name = request.args.get('color')
    if color_name and color_name.lower() in matplotlib.colors.CSS4_COLORS:
        hex_code = matplotlib.colors.CSS4_COLORS[color_name.lower()]
        return {"hex_code": hex_code}
    else:
        return {"error": "Invalid color name"}, 400