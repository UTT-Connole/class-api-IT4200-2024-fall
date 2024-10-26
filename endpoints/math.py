from flask import Blueprint, jsonify, request
import math

math_bp = Blueprint('math', __name__)

factorialCache = {}
@math_bp.route('/factorial', methods=['GET'])
def factorial():
    n = request.args.getlist('n', type=int)
    as_string = request.args.get('as_string', 'false').lower() == 'true'
    max_allowed = 1000 

    if not n:
        return jsonify({"error": "No input provided"}), 400

    resultList = []

    for num in n:
        if num < 0:
            return jsonify({"error": f"No negative numbers: {num}"}), 400
        
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
    base = request.args.get('base', type=float)
    exp = request.args.get('exp', type=float)

    if base == 0 and exp < 0:
        return "Cannot raise 0 to a negative number", 400

    if base is None or exp is None:
        return "Invalid Input", 400
    result = base ** exp
    return jsonify(result=result), 200
