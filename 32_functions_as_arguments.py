def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculate(operation, a, b):
    return operation(a, b)

a = float(input("First number: "))
b = float(input("Second number: "))
print("Addition:", calculate(add, a, b))
print("Subtraction:", calculate(subtract, a, b))
print("Multiplication:", calculate(multiply, a, b))
print("Division:", calculate(divide, a, b))
