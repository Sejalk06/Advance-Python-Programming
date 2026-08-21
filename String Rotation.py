
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Yes, it is a rotation.")
else:
    print("No, it is not a rotation.")
