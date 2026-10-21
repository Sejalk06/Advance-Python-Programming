def is_palindrome(value):
    text = str(value).lower().replace(" ", "")
    return text == text[::-1]

value = input("Enter a string or number: ")
print(is_palindrome(value))
