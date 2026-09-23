
arr = [1,2,3,5,9]

missing_num = []
for number in range(min(arr), max(arr)+1):
  if number not in arr:
    missing_num.append(number)

print(missing_num)

'''
output:
[4, 6, 7, 8]
'''
