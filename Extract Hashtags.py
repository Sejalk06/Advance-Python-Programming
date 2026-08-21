import re

def extract_hashtags(post_text):
    hashtag_pattern = r'#\w+'
    return re.findall(hashtag_pattern, post_text)

sample_post = "Loving the weather today! #sunny #good_vibes #weekend2026"
print(extract_hashtags(sample_post))
