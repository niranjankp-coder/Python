# examples/search_methods.py

text = "Hello World Hello"

# find() - Returns index, -1 if not found
print(text.find("World"))      # 6
print(text.find("Python"))     # -1

# rfind() - Search from right
print(text.rfind("Hello"))     # 12

# index() - Like find but raises error
print(text.index("World"))     # 6
# text.index("Python")         # ValueError!

# rindex() - Search from right
print(text.rindex("Hello"))    # 12

# count() - Count occurrences
print(text.count("Hello"))     # 2

# startswith() - Check beginning
print(text.startswith("Hello"))  # True
print(text.startswith("World"))  # False

# endswith() - Check ending
print(text.endswith("Hello"))    # True
print(text.endswith("World"))    # False
