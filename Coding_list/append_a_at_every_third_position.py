list_l = [1,5,7,3,8,11,3,77,8]

size = len(list_l)-1
output = []
value = "a"

for x in range(0, size, 3):
    y = x+1
    output.append(list_l[x])
    output.append(list_l[y])
    output.append(value)
print(output)


'''
output
[1, 5, 'a', 3, 8, 'a', 3, 77, 'a']
'''
