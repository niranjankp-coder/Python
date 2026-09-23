# Flatten Nested List
lst = [[1,2],[3,4],[5,6]]

output = []
for x in lst:
  output.extend(x)
print(output)

'''
output:

[1, 2, 3, 4, 5, 6]
'''
