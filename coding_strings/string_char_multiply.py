'''
WAP for the follwoing requirement
input = "a4b3c2"
output = "aaaabbbcc"
'''

inp = "a4b3c2"
output = ""
for char in inp:
    if char.isalpha():
        char_local = char
    elif char.isdigit():
        output+= char_local*int(char)
print(output)
