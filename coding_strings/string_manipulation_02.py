'''
write a program for the following requirement
input = a4k3b2
output = aeknbd
'''

input_str = "a4k3b2"
output = ""
for char in input_str:
    if char.isalpha():
        value_char = ord(char)
        output+= char
    elif char.isdigit():
        value2 = value_char+int(char)
        output+= chr(value2)
print(output)
