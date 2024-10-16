from flask import Blueprint, request, jsonify, render_template

calc_bp = Blueprint('calc', __name__)

@calc_bp.route('/calc', methods=['GET'])
def calc_main():
    x = request.args.get('x')
    y = request.args.get('y')
    op = request.args.get('op')
    
    if not x and not y and not op:
        return render_template('calc.html')
    
    if not op:
        return jsonify({"error": "Invalid Input"}), 400
    
    # Replace blanks with 0
    x = 0 if x is None or x == '' else x
    y = 0 if y is None or y == '' else y
    
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return jsonify({"error": "Invalid Input"}), 400
    
    operations = {
        'add': x + y,
        'subtract': x - y,
        'multiply': x * y,
        'divide': (x / y if y != 0 else "You cannot divide by 0"),
        'mod': (x % y if y != 0 else "You cannot take modulus by 0"),
        'square': x * x,
        'sqrt': (x ** 0.5 if x >= 0 else "Cannot take square root of a negative number"),
        'decimal': (bin(x).replace("0b","") if x >= 0 else "Not compatible with negative input"),
        'binary': ((str(int(str(x), 2))) if all(c in '01' for c in str(x)) and x >= 0 else "Not compatible format to convert to binary"),
        'power': x ** y,
        'cube': x ** 3
    }

    if op not in operations:
        available_operations = ', '.join(operations.keys())
        return jsonify({"error": f"Invalid operation. Available operations are: {available_operations}"}), 400
    
    result = operations[op]

    if 'text/html' in request.headers.get('Accept', ''):
        return render_template('calc.html', result=result)
    
    return jsonify({"result": result})

@calc_bp.route('/calcop', methods=['GET'])
def calc_operators():
    operations = ['add', 'subtract', 'multiply', 'divide', 'mod', 'square', 'sqrt', 'decimal', 'binary', 'power', 'cube']
    return jsonify(operations)