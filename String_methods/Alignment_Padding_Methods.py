text = "Hello"

# center() - Center align
print(text.center(20))         # "       Hello        "
print(text.center(20, "*"))    # "*******Hello********"

# ljust() - Left align
print(text.ljust(20))          # "Hello               "
print(text.ljust(20, "-"))     # "Hello---------------"

# rjust() - Right align
print(text.rjust(20))          # "               Hello"
print(text.rjust(20, "-"))     # "---------------Hello"

# zfill() - Pad with zeros on left
print("42".zfill(5))           # "00042"
print("-42".zfill(5))          # "-0042"
