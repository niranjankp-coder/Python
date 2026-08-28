# examples/string_methods.py

text = "   Hello World   "

# strip() - Remove both sides whitespace
print(text.strip())           # "Hello World"

# lstrip() - Remove left whitespace
print(text.lstrip())          # "Hello World   "

# rstrip() - Remove right whitespace
print(text.rstrip())          # "   Hello World"

# Strip specific characters
text2 = "###Hello###"
print(text2.strip("#"))       # "Hello"
print(text2.lstrip("#"))      # "Hello###"
print(text2.rstrip("#"))      # "###Hello"
