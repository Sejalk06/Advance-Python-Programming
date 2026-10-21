def binary_search(items, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if items[mid] == target:
        return mid
    if target < items[mid]:
        return binary_search(items, target, low, mid - 1)
    return binary_search(items, target, mid + 1, high)

items = sorted(map(int, input("Enter sorted-list numbers: ").split()))
target = int(input("Enter number to search: "))
print("Index =", binary_search(items, target, 0, len(items) - 1))
