from flask import Blueprint,jsonify

api=Blueprint('api',__name__)

@api.route('/health',methods=['GET'])
def health_check():
    return jsonify({"status":"Healthy"}),200


@api.route('/multiply', methods=['POST'])
def multiply():
    data = {"a": 5, "b": 3}  # Example payload
    result = data['a'] * data['b']
    return jsonify({"result": result}), 200