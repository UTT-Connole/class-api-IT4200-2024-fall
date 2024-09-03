from flask import Flask, request
import random
import matplotlib

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/calc', methods=['GET','POST'])
def calc_main():
    x = request.args.get('x')
    y = request.args.get('y')
    if x and y:
        x = int(x)
        y = int(y)
        result = x+y
    else:
        result = "Invalid Input"
    return str(result)

@app.route('/color', methods=['GET','POST'])
def color_hexifier():
    color_name = request.args.get('color')
    
    print(f"Received color name: {color_name}")
    
    if color_name and color_name.lower() in matplotlib.colors.CSS4_COLORS:
        hex_code = matplotlib.colors.CSS4_COLORS[color_name.lower()]
        return f"The hex code for {color_name} is {hex_code}"
    else:
        return "Invalid color name"
