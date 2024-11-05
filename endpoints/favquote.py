# endpoints/quotes.py

from flask import Blueprint, request, jsonify

quotes_bp = Blueprint("quotes", __name__)

@quotes_bp.route('/favoritequote', methods=['GET', 'POST', 'PATCH'])
def get_favorite_quote():
    favorite_quote = {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs"
    }
    quotes = [favorite_quote]

    if request.method == 'GET':
        return jsonify(favorite_quote)

    elif request.method == 'POST':
        new_quote = request.json
        quotes.append(new_quote)
        return jsonify({"message": "New favorite quote added!", "quote": new_quote}), 201

    elif request.method == 'PATCH':
        # Assuming the client sends the author's name to identify which quote to update
        author = request.json.get('author')
        updated_quote = request.json.get('quote')

        for quote in quotes:
            if quote['author'] == author:
                quote['quote'] = updated_quote
                return jsonify({"message": "Favorite quote updated!", "quote": quote}), 200

        return jsonify({"error": "Quote not found for the given author."}), 404
