'''
find the number of occurences of each character present in given string with count()
'''

s = "AABACC DDDGD KJAA"

output = {}
for char in s:
    if char == " ":
        continue
    if char not in output:
        value = s.count(char)
        output[char] = value
print(output)
