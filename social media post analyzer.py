import re

def extract_hashtags(text):
    hashtags = re.findall(r'#[A-Za-z0-9_]+', text)
    return hashtags

text = input("Enter your social media post: ")

result = extract_hashtags(text)

print("Hashtags:", result) 
