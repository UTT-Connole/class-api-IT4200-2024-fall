from flask import Blueprint, request, jsonify, render_template

calc_bp = Blueprint('calc', __name__)

@calc_bp.route('/calc', methods=['GET', 'POST'])
def calc_main():
    x = request.args.get('x')
    y = request.args.get('y')
    op = request.args.get('op')
    
    if not op:
        return render_template('calc.html', result="Invalid Input")
    
    # Replace blanks with 0
    x = 0 if x is None or x == '' else x
    y = 0 if y is None or y == '' else y
    
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return render_template('calc.html', result="Invalid Input")
    
    operations = {
        'add': x + y,
        'subtract': x - y,
        'multiply': x * y,
        'divide': (x / y if y != 0 else "You cannot divide by 0"),
        'mod': (x % y if y != 0 else "You cannot take modulus by 0"),
        'square': x * x,
        'sqrt': (x ** 0.5 if x >= 0 else "Cannot take square root of a negative number")
    }

    if op not in operations:
        available_operations = ', '.join(operations.keys())
        return render_template('calc.html', result=f"You might have spelled something wrong or there is not the option. The current options are: {available_operations}")
    
    result = operations[op]
    return render_template('calc.html', result=str(result))

# For the tests in testing/test_calc.py to get the operations
@calc_bp.route('/calcop', methods=['GET'])
def calc_operators():
    operations = ['add', 'subtract', 'multiply', 'divide', 'mod', 'square', 'sqrt']
    return jsonify(operations)