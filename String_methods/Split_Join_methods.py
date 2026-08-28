# examples/split_join_methods.py

text = "Hello,World,Python,Django"

# split() - Split into list
print(text.split(","))
# ['Hello', 'World', 'Python', 'Django']

# split with maxsplit
print(text.split(",", 2))
# ['Hello', 'World', 'Python,Django']

# rsplit() - Split from right
print(text.rsplit(",", 1))
# ['Hello,World,Python', 'Django']

# splitlines() - Split by line breaks
multi = "Line1\nLine2\nLine3"
print(multi.splitlines())
# ['Line1', 'Line2', 'Line3']

# join() - Join list into string
words = ["Hello", "World", "Python"]
print(" ".join(words))        # "Hello World Python"
print("-".join(words))        # "Hello-World-Python"
print("".join(words))         # "HelloWorldPython"
