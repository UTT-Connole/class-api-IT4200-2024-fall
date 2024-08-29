from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/calc')
def calc_main():
    return "This is the starter page for the calculator app"