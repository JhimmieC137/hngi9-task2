from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from arithmetic import addition, subtraction, multiplication, str_math


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
  
    
    
    
@app.route('/')
def home():
    slack_username = "jimi"
    age = 24
    bio = "I am curious about how things work"
    return jsonify ({
        "slackUsername": slack_username,
        "backend": True,
        "age": age,
        "bio": bio
    })


@app.route('/tasks/2', methods=['POST'])
def enum_task():
    payload = request.get_json()
    try:
        add = "add"
        sub = "subtract"
        mult = "multi"
        operation = payload.get('operation_type')
        X = payload.get('x')
        Y = payload.get('y')
        slack_user = 'Jimi'
        
        if operation == 'addition':
            final_result = addition(X, Y)
        elif operation == 'subtraction':
            final_result = subtraction(X, Y)
        elif operation == 'multiplication':
            final_result = multiplication(X, Y)
        else:
            final_result = str_math(operation)
                      
            
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
    
    

if __name__ == "__main__":
    app.run()