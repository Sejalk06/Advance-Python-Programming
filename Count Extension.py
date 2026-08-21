import re

def count_extensions(files):
    extensions = {}

    for file in files:
        match = re.search(r'\.[A-Za-z0-9]+$', file)

        if match:
            ext = match.group()
            extensions[ext] = extensions.get(ext, 0) + 1

    return extensions

files = input("Enter filenames separated by spaces: ").split()

result = count_extensions(files)

print("Extension count:", result)
