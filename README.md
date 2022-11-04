# hngi9-task2

## This task was to create an app with a POST enpoint that:
- Takes in a json body of an operation type(addition, subtraction, multiplication) and two integears(x and y)
- Performs a simple arithmetic operation with the two integers using the opertion type
- Returns a json reponse that'll include a slack username, result, and the operation type 

This app will be deployed to a server

## Running the application
To run the application, clone or download the repo, create a virtual environment and navigate to the Task-2 folder. In the terminal, pip install the requirements with the command:

`pip install requirements.txt`  

Then run the following commands to run the application on your localhost

`export FLASK_APP=app.py <br>
export FLASK_DEBUG=true  <br>
flask run`

The required json payload format is 

`{'operation_type':'<addition|subtraction|multiplication>', 'x': int, 'y': int}`

The deplopyed app can by found [here](https://jimi.theupfolio.com/tasks/2)
