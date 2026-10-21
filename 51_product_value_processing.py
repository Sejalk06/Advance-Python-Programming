products = [("Pen", 20, 10), ("Bag", 1200, 2), ("Book", 150, 5)]
values = list(map(lambda p: (p[0], p[1] * p[2]), products))
costly = list(filter(lambda item: item[1] > 1000, values))
sorted_values = sorted(values, key=lambda item: item[1])
print("Total value of products =", values)
print("Products costing more than 1000 =", costly)
print("Sorted by total value =", sorted_values)
