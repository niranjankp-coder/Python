'''
write a program to generate words from given inputs strings by taking characters
alternatively
'''

s1 = "abcdefg"
s2 = "xyz"
s3 = "12345"

output = ""
i = j = k = 0

while i <= len(s1)-1 or j <= len(s2)-1 or k <= len(s3):
    if i < len(s1):
        output+= s1[i]
    if j < len(s2):
        output+= s2[j]
    if k < len(s3):
        output+= s3[k]
    i+=1
    j+= 1
    k+= 1
print(output)
