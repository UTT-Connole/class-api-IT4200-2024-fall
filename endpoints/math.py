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
        return jsonify({"error": "Invalid Input"}), 400
    
    
    x = 0 if x is None or x == '' else x
    y = 0 if y is None or y == '' else y
    
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return jsonify({"error": "Invalid Input"}), 400
    if abs(x) > 10**6 or abs(y) > 10**6:
        return jsonify({"error": "Input out of bounds"}), 400
    
    if op == 'divide':
        if y == 0:
            return jsonify({"error": "You cannot divide by 0"}), 400
        result = x / y
        
    elif op == 'mod':
        if y == 0:
            return jsonify({"error": "You cannot take modulus by 0"}), 400
        result = x % y
    
    elif op == 'sqrt':
        if x < 0:
            return jsonify({"error": "Cannot take square root of a negative number"}), 400
        result = x ** 0.5
    
    
    else:
        operations = {
            'add': x + y,
            'subtract': x - y,
            'multiply': x * y,
            'divide': (x / y if y != 0 else jsonify({"error":"You cannot divide by 0"}), 400),
            'mod': (x % y if y != 0 else jsonify({"error":"You cannot take modulus by 0"}), 400),
            'square': x * x,
            'sqrt': (x ** 0.5 if x >= 0 else jsonify({"error":"Cannot take square root of a negative number"}), 400),
            'decimal': (bin(x).replace("0b", "") if x >= 0 else "Not compatible with negative input"),
            'binary': (str(int(str(x), 2)) if all(c in '01' for c in str(x)) and x >= 0 else "Not compatible format to convert to binary"),
            'power': (x ** y if abs(x ** y) < 10**6 else "Result too large"),
            'cube': x ** 3,
            'log': (math.log(x, y) if y != 0 else math.log(x, 10)) if x > 0 else "Cannot take logarithm of zero or negative number",
            'exp': x ** y
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
    operations = ['add', 'subtract', 'multiply', 'divide', 'mod', 'square', 'sqrt', 'decimal', 'binary', 'power', 'cube', 'log', 'exp']
    return jsonify(operations)

factorialCache = {}
@math_bp.route('/factorial', methods=['GET'])
def factorial():
    n = request.args.getlist('n', type=int)
    as_string = request.args.get('as_string', 'false').lower() == 'true'
    max_allowed = 1000 

    if not n:
        return jsonify({"error": "No input provided"}), 400
    
    if len(n) > 10:
        return jsonify({"error": "too many inputs please provide up to 10"}), 400

    resultList = []

    for num in n:
        if num < 0:
            return jsonify({"error": f"No negative numbers: {num}"}), 400
        
        if num > max_allowed:
            return jsonify({"error": f"Number too large: {num}. Maximum allowed is {max_allowed}."}), 400
        
        if num in factorialCache:
            result = factorialCache[num]
        else:
            result = math.factorial(num)
            factorialCache[num] = result
        
        resultList.append(result)

    if len(resultList) == 1:
        return jsonify(result=resultList[0]), 200 
    else:
        return jsonify(result=resultList), 200
    
@math_bp.route('/power', methods=['GET'])
def power():
    # First, try to get the 'base' as a list from getlist. If it's a list of comma-separated values, split them.
    base_list = request.args.getlist('base')
    exp = request.args.get('exp', type=float)
    notation = request.args.get('notation', 'default').lower()
    precision = request.args.get('precision', type=int, default=6)

    if not base_list or exp is None:
        return jsonify({"error": "Base and exponent must be provided"}), 400

    # Handle if base_list contains a single comma-separated string, split it
    if len(base_list) == 1 and ',' in base_list[0]:
        base_list = base_list[0].split(',')

    # Validate precision range
    if precision < 0 or precision > 20:
        return jsonify({"error": "Precision must be between 0 and 20"}), 400

    calculations = []

    for base_value in base_list:
        try:
            base = float(base_value)
        except ValueError:
            return jsonify({"error": "Invalid base value(s)"}), 400

        # Handle the case of zero raised to a negative exponent
        if base == 0 and exp < 0:
            return jsonify({"error": "Cannot raise 0 to a negative power"}), 400

        # Handle fractional exponents for negative bases
        if base < 0 and exp % 1 != 0:
            return jsonify({"error": "Cannot raise negative numbers to fractional powers"}), 400

        try:
            result = base ** exp
            if notation == 'scientific':
                result = f"{result:.{precision}e}"
            else:
                result = f"{result:.{precision}f}"

            calculations.append({
                "base": base,
                "exponent": exp,
                "result": result,
                "notation": notation
            })
        except ValueError as ve:
            return jsonify({"error": f"Invalid calculation for base {base}: {str(ve)}"}), 400

    # If only one calculation, return a single result
    if len(calculations) == 1:
        return jsonify(calculations[0]), 200
    else:
        return jsonify(calculations=calculations), 200