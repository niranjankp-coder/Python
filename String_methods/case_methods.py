# examples/case_methods.py

text = "hello world"

# upper() - Convert to uppercase
print(text.upper())          # "HELLO WORLD"

# lower() - Convert to lowercase
print("HELLO".lower())       # "hello"

# capitalize() - First letter capital
print(text.capitalize())     # "Hello world"

# title() - Each word capitalized
print(text.title())          # "Hello World"

# swapcase() - Swap upper and lower
print("Hello World".swapcase())  # "hELLO wORLD"

# casefold() - Aggressive lowercase (for comparison)
print("Straße".casefold())   # "strasse"
