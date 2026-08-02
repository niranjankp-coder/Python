'''
Program to remove duplicates characters from the given string
'''

input_str = "aazzssddffgggghhh"

output = ""

for char in input_str:
    if char not in output:
        output+= char
print(output)
