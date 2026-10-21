numbers = list(map(int, input("Enter numbers: ").split()))
print(list(filter(lambda n: n > 0, numbers)))
