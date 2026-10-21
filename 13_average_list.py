def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Average =", average(numbers))
