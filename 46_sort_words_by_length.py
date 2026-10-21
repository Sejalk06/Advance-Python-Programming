words = input("Enter words separated by spaces: ").split()
print(sorted(words, key=lambda word: len(word)))
