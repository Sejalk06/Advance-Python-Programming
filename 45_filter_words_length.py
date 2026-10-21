words = input("Enter words separated by spaces: ").split()
print(list(filter(lambda word: len(word) > 5, words)))
