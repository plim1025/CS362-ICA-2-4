def addition(a, b):
    if (not isinstance(a, int) and not isinstance(a, float)) or (not isinstance(b, int) and not isinstance(b, float)):
        print("Invalid input")
        return None
    return a + b

def subtraction(a, b):
    if (not isinstance(a, int) and not isinstance(a, float)) or (not isinstance(b, int) and not isinstance(b, float)):
        print("Invalid input")
        return None
    return a - b

def multiplication(a, b):
    if (not isinstance(a, int) and not isinstance(a, float)) or (not isinstance(b, int) and not isinstance(b, float)):
        print("Invalid input")
        return None
    return a * b

def division(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        print("Invalid input")
        return None
    if b == 0:
        print("Cannot divide by zero")
        return None
    return a / b
