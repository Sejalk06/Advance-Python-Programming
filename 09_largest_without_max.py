def largest(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Largest =", largest(numbers))
