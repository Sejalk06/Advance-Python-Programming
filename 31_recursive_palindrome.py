def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

text = input("Enter a string: ").lower().replace(" ", "")
print(is_palindrome(text))
