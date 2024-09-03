from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

def dad_joke():
    joke = {
        "joke": "Why don't skeletons fight each other? They don't have the guts."
    }
    return jsonify(joke)

