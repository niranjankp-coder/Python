# is___() methods - Return True or False

# isalpha() - Only letters
print("Hello".isalpha())       # True
print("Hello123".isalpha())    # False

# isdigit() - Only digits
print("12345".isdigit())       # True
print("123.45".isdigit())      # False

# isnumeric() - Numeric characters
print("12345".isnumeric())     # True
print("½".isnumeric())         # True (fraction)

# isalnum() - Letters and numbers only
print("Hello123".isalnum())    # True
print("Hello 123".isalnum())   # False (space)

# isspace() - Only whitespace
print("   ".isspace())         # True
print("  a  ".isspace())       # False

# isupper() - All uppercase
print("HELLO".isupper())       # True
print("Hello".isupper())       # False

# islower() - All lowercase
print("hello".islower())       # True

# istitle() - Title case check
print("Hello World".istitle()) # True
print("Hello world".istitle()) # False

# isidentifier() - Valid Python variable name
print("hello".isidentifier())  # True
print("123hello".isidentifier()) # False

# isprintable() - All printable chars
print("Hello".isprintable())   # True
print("Hello\n".isprintable()) # False
