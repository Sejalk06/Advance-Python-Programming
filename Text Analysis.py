text = input("Enter a paragraph:\n")

words = text.lower().split()

print("\nTotal Words =", len(words))

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies")
for word in frequency:
    print(word, ":", frequency[word])

sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("\nTop 3 Frequent Words")
for i in range(min(3, len(sorted_words))):
    print(sorted_words[i][0], ":", sorted_words[i][1])

vowels = "aeiou"
count = 0

for ch in text.lower():
    if ch in vowels:
        count += 1

print("\nTotal Vowels =", count)
