def second_largest(numbers):
    unique = sorted(set(numbers))
    if len(unique) < 2:
        return "Second-largest number does not exist"
    return unique[-2]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Second largest =", second_largest(numbers))
