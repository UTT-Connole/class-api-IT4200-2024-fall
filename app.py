from flask import Flask, request
import random


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