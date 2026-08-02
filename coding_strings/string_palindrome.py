'''
write a program to check whether the given string is palindrome
'''

str = input("ENTER THE INPUT STRING: ").strip()
size = len(str)-1
rev_str = ""
while size >= 0:
    rev_str+= str[size]
    size-= 1
if str == rev_str:
    print("it's palindrome")
else:
    print("it's not a palindrome!!!")
