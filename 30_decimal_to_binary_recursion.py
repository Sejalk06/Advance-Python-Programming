def decimal_to_binary(n):
    if n < 2:
        return str(n)
    return decimal_to_binary(n // 2) + str(n % 2)

n = int(input("Enter a non-negative decimal number: "))
print("Binary =", decimal_to_binary(n))
