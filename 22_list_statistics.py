def statistics(numbers):
    return min(numbers), max(numbers), sum(numbers), sum(numbers) / len(numbers)

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
smallest, biggest, total, avg = statistics(numbers)
print("Minimum =", smallest)
print("Maximum =", biggest)
print("Sum =", total)
print("Average =", avg)
