'''
write a program to find the whether give two strings are anagram
'''

input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

if sorted(input_str1.lower()) == sorted(input_str2.lower()):
    print("Two strings are anagram")
else:
    print("Two strings are not anagram")
