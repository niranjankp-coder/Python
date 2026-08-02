# write a program to reverse a string

input_str = "PYTHON"
size = len(input_str)-1
output = ""
while size >= 0:
    output+= input_str[size]
    size-= 1
print(f"output of the input reverse string is:'{output}'")
