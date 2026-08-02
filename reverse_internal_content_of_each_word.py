# write a program to reverse internal content of each word

input_str = "Learning python is very easy"
list_inp = input_str.split()
output = []
for word in list_inp:
    size = len(word)-1
    output_inst = ""
    while size >= 0:
        output_inst+= word[size]
        size-=1
    output.append(output_inst)
    output_inst = ""
print(' '.join(output))
