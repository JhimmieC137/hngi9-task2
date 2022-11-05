import math

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

def str_math(operation):
    add = "add"
    sub = "subtract"
    mult = "multi"
    
    if add in operation:
        result = sum([int(number) for number in operation.split() if number.isdigit()]) 

    elif sub in operation:
        step = [int(number) for number in operation.split() if number.isdigit()]
        if "from" in operation:
            result = step[1] - step[0]
        else:
            result = step[0] - step[1]
        
    elif mult in operation:
        step = [int(number) for number in operation.split() if number.isdigit()]
        result = math.prod(step)
    
    return result