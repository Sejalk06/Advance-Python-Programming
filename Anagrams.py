import string

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Convert to lowercase
str1 = str1.lower()
str2 = str2.lower()

# Remove spaces and punctuation
for ch in string.punctuation + " ":
    str1 = str1.replace(ch, "")
    str2 = str2.replace(ch, "")

if sorted(str1) == sorted(str2):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")
