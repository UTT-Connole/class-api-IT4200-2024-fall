from flask import Blueprint, request, jsonify, render_template
import math

math_bp = Blueprint('math', __name__)

@math_bp.route('/calc', methods=['GET'])
def calc_main():
    x = request.args.get('x')
    y = request.args.get('y')
    op = request.args.get('op')

    if not x and not y and not op:
        return render_template('calc.html')

    if not op:
        return jsonify({"error": "Missing operation"}), 400

    # Handle empty x or y cases
    if not x or x == '':
        return jsonify({"error": "Missing input x"}), 400
    if y is None or y == '':  # y can be optional for some operations
        y = 0

    try:
        x = float(x)  # Allow x to be a float (decimal input)
        y = float(y)  # Allow y to be a float (decimal input)
    except ValueError:
        return jsonify({"error": "Invalid Input"}), 400

    # Ensure x is an integer where necessary (binary, decimal)
    if op in ['binary', 'decimal']:
        if not x.is_integer():
            return jsonify({"error": "Invalid Input. Must be a number."}), 400
        if x < 0:
            return jsonify({"result": "Not compatible with negative input"}), 200

    operations = {
        'add': x + y,
        'subtract': x - y,
        'multiply': x * y,
        'divide': (x / y if y != 0 else "You cannot divide by 0"),
        'mod': (x % y if y != 0 else "You cannot take modulus by 0"),
        'square': x * x,
        'sqrt': (x ** 0.5 if x >= 0 else "Cannot take square root of a negative number"),
        'decimal': (bin(int(x)).replace("0b", "") if x >= 0 and x.is_integer() else "Not compatible with negative input"),
        'binary': (str(int(str(int(x)), 2)) if all(c in '01' for c in str(int(x))) else "Not compatible format to convert to binary"),
        'power': x ** y,
        'cube': x ** 3,
        'exp': math.exp(x)  # New exponential function
    }

    if op not in operations:
        available_operations = ', '.join(operations.keys())
        return jsonify({"error": f"Invalid operation. Available operations are: {available_operations}"}), 400

    result = operations[op]

    if 'text/html' in request.headers.get('Accept', ''):
        return render_template('calc.html', result=result)

    return jsonify({"result": result})

@math_bp.route('/calcop', methods=['GET'])
def calc_operators():
    operations = ['add', 'subtract', 'multiply', 'divide', 'mod', 'square', 'sqrt', 'decimal', 'binary', 'power', 'cube', 'exp']
    return jsonify(operations)
