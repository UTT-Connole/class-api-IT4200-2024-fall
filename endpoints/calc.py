from flask import Blueprint, request

calc_bp = Blueprint('calc', __name__)

@calc_bp.route('/calc', methods=['GET', 'POST'])
def calc_main():
    x = request.args.get('x')
    y = request.args.get('y')
    op = request.args.get('op')
    
    if not (x and y and op):
        return "Invalid Input"
    
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return "Invalid Input"
    
    operations = {
        'add': x + y,
        'subtract': x - y,
        'multiply': x * y,
        'divide': x / y if y != 0 else "You cannot divide by 0",
        'mod': x % y if y != 0 else "You cannot take modulus by 0"
    }
    
    if op not in operations:
        available_operations = ', '.join(operations.keys())
        return f"You might have spelled something wrong or there is not the option. The current options are: {available_operations}"
    
    result = operations[op]
    
    return str(result)