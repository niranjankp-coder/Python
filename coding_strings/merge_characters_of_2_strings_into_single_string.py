'''
write a program to merge characters of 2 strings into single string by taking
alternative characters 
precondition: input string must be same length
'''

s1 = "RAVI"
s2 = "TEJA"

output = ""
i = 0
j = 0
i_index = len(s1)-1
j_index = len(s1)-1
while i <= i_index and j <= j_index:
    output+= s1[i]+s2[j]
    i+= 1
    j+= 1
print(output)
    


    
    
        
        
    

    


