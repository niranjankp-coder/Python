# format() - String formatting
name = "Niranjan"
age = 25
print("My name is {} and age is {}".format(name, age))
# "My name is Niranjan and age is 25"

# format with index
print("Name: {0}, Age: {1}, Again: {0}".format(name, age))

# format with keywords
print("Name: {name}, Age: {age}".format(name="Niranjan", age=25))

# format_map() - Format using dictionary
data = {"name": "Niranjan", "city": "Bangalore"}
print("Name: {name}, City: {city}".format_map(data))

# encode() - Encode string to bytes
text = "Hello"
print(text.encode("utf-8"))    # b'Hello'
print(text.encode("ascii"))    # b'Hello'
