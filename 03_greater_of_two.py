def greater(a, b):
    if a > b:
        return a
    return b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Greater number =", greater(a, b))
