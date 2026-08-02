'''
WAP for the follwoing requirement
input = "aaaabbbccz"
output = "4a3b2c1z"
'''
input_str = "aaaabbbccz"
output = ""
for x in input_str:
    if x not in output:
        value = input_str.count(x)
        value_res = str(value)+x
        output+= value_res
print(output)
