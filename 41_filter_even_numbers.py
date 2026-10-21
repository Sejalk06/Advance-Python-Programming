numbers = list(map(int, input("Enter integers: ").split()))
print(list(filter(lambda n: n % 2 == 0, numbers)))
