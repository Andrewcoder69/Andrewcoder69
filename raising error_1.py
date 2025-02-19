def divide(x, y):
    if y == 0:
        raise ZeroDivisionError('Cannot divide by zero!')
    return x/y

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f'An error occured: {e}')
    
