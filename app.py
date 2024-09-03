from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/quotes', methods=['GET'])
def favoriteQuotes():
        quotes = '''
        [
            {"quote": "If more of us valued food and cheer and song above hoarded gold, it would be a merrier world.", "author": Thorin Oakenshield}
        ]'''
        return quotes