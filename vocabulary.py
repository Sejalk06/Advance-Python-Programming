# Vocabulary Analysis

book1 = input("Enter text of Book 1:\n").lower().split()
book2 = input("\nEnter text of Book 2:\n").lower().split()

set1 = set(book1)
set2 = set(book2)

print("\nUnique words in Book 1:")
print(set1)

print("\nUnique words in Book 2:")
print(set2)

print("\nCommon words:")
print(set1.intersection(set2))

print("\nWords only in Book 1:")
print(set1.difference(set2))

print("\nWords only in Book 2:")
print(set2.difference(set1))

print("\nTotal unique words across both books:")
print(len(set1.union(set2)))
