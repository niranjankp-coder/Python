# Find Even Numbers Using List Comprehension
nums= [1,2,3,4,5,6]

out = [x for x in nums if x%2 ==0]
print(f"Even numbers are: \n output: \n {out}")

'''
Even numbers are: 
 output: 
 [2, 4, 6]
'''
