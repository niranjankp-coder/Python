'''
input character contains mix of alpha and numneric, 
WAP to sort characters of the string
pre-condition: first alphabets followed by digits
'''
inp = "B4A1D3"
out_alpha = ""
out_digits = ""
for char in inp:
    if char.isalpha():
        out_alpha+= char
    elif char.isdigit():
        out_digits+= char
output = ''.join(sorted(out_alpha)+sorted(out_digits))
print(output)
