from main import error

def result(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return  a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    elif operation == '**':
        return a ** b
    else:
        return error()