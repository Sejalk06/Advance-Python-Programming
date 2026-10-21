a = list(map(int, input("First list: ").split()))
b = list(map(int, input("Second list: ").split()))
print(list(map(lambda x, y: x + y, a, b)))
