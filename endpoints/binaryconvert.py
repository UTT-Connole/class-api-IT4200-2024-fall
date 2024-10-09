from flask import Blueprint, request

# Create a blueprint for convertToBinary
convertToBinary_bp = Blueprint('convertToBinary', __name__)

@convertToBinary_bp.route('/convertToBinary', methods=['GET','POST'])
def convertToBinary():
    num = request.args.get('num')
    type = request.args.get('type')
    
    if type == 'decimal':
        try:
            num = int(num)
            if num >= 0:
                return bin(num).replace("0b","")
            else:
                return "Not compatible with negative input"

        except:
            try:
                num = float(num)
                if isinstance(num,float):
                    return "Not compatible with float input"
            except:
                return "Please input a valid number"
            
    elif type == 'binary':
        try:
            num = int(num)
            if num >= 0:
                num = str(num)
                return str(int(num, 2))
            else:
                return "Not compatible with negative input"
            
        except:
            try:
                num = float(num)
                if isinstance(num,float):
                    return "Not compatible with float input"
            except:
                return "Please input a valid number"
            
    else:
        return 'Invalid Type. Please use [decimal] for Decimal to Binary converstions and [binary] for Binary to Decimal converstions'