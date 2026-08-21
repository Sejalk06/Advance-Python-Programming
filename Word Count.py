import re

filename = input("Enter file name: ")

file = open(filename, "r")
text = file.read()
file.close()

text = text.lower()
words = re.findall(r'\b\w+\b', text)

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("Total number of words:", len(words))
print("Top 10 most frequent words:")

for word, count in sorted_words[:10]:
    print(word, ":", count)
