from flask import Blueprint, request

# Create a blueprint for convertToBinary
convertToBinary_bp = Blueprint('convertToBinary', __name__)

@convertToBinary_bp.route('/convertToBinary', methods=['GET','POST'])
def convertToBinary():
    num = request.args.get('num')
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