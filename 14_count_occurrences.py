def count_occurrences(items, element):
    count = 0
    for item in items:
        if item == element:
            count += 1
    return count

items = input("Enter items separated by spaces: ").split()
element = input("Enter item to count: ")
print("Occurrences =", count_occurrences(items, element))
