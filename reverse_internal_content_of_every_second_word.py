'''
write a program to reverse internal content of every second word
present in the given string
'''
input_str = "Learning python is very easy"

input_list =input_str.split()
index_input = 0
output = []
while index_input <= len(input_list)-1:
    if index_input % 2 != 0:
        rev_inst = (input_list[index_input])[::-1]
        output.append(rev_inst)
    else:
        output.append(input_list[index_input])
    index_input+= 1
print(output)
