# write a program to reverse order of words

input_str = "Learning python is very easy"

output = []
list_input = input_str.split()
size = len(list_input)-1

while size >= 0:
    output.append(list_input[size])
    size-=1
print(" ".join(output))
