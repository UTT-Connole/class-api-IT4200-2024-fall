import requests
import matplotlib, math
from flask import Blueprint, jsonify, render_template

@color_bp.route('/color', methods=['GET','POST'])
    def color_hexifier():
        color_name = request.args.get('color')
    
        print(f"Received color name: {color_name}")
    
        if color_name and color_name.lower() in matplotlib.colors.CSS4_COLORS:
            hex_code = matplotlib.colors.CSS4_COLORS[color_name.lower()]
            return f"The hex code for {color_name} is {hex_code}"
        else:
            return "Invalid color name"