from flask import Flask, jsonify, request, abort
from flask_cors import CORS


def addition(first, second):
    result = first + second
    return result

def subtraction(first, second):
    if first > second:
        result = first - second
    elif second > first:
        result = second - first
    else: 
        result = 0
    return result

def multiplication(first, second):
    result = first * second
    return result



app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# CORS Headers
@app.after_request
def after_request(response):
    response.headers.add(
        "Access-Control-Allow-Headers", "Content-Type, Authorization, true"
    )
    response.headers.add(
        "Access-Control-Allow-Methods", "GET, POST"
    )
    return response
    
    


@app.route('/tasks/2', methods=['POST'])
def enum_task():
    payload = request.get_json()
    try:
        operation = payload.get('operation_type')
        X = payload.get('x')
        Y = payload.get('y')
        slack_user = 'Jimi'
        
        if operation == 'addition':
            final_result = addition(X, Y)
        elif operation == 'subtraction':
            final_result = subtraction(X, Y)
        else:
            final_result = multiplication(X, Y)
            
        return jsonify ({
            'slackUsername': slack_user,
            'result': final_result,
            'operation_type': operation
        })

            
        
    except:
        abort(405)
        
@app.errorhandler(405)
def bad_request(error):
    return jsonify ({
        'success': False,
        'error': 405,
        'message': 'Method not allowed'
    }), 405