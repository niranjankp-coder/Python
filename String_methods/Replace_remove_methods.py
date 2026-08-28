text = "Hello World Hello Python"

# replace() - Replace substring
print(text.replace("Hello", "Hi"))
# "Hi World Hi Python"

# replace with count limit
print(text.replace("Hello", "Hi", 1))
# "Hi World Hello Python"

# removeprefix() - Python 3.9+
text3 = "Hello_World"
print(text3.removeprefix("Hello_"))   # "World"

# removesuffix() - Python 3.9+
print(text3.removesuffix("_World"))   # "Hello"
