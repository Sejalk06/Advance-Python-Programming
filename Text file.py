import re

filename = input("Enter file name: ")
target = input("Enter word or phrase to find: ")
replacement = input("Enter replacement: ")
choice = input("Case sensitive? (yes/no): ")

file = open(filename, "r")
text = file.read()
file.close()

if choice.lower() == "yes":
    text = text.replace(target, replacement)
else:
    text = re.sub(re.escape(target), replacement, text, flags=re.IGNORECASE)

new_file = input("Enter new file name: ")

file = open(new_file, "w")
file.write(text)
file.close()

print("File updated successfully.")
