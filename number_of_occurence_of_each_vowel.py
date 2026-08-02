'''
Write a program to find the number of occurence of each vowel in the input 

'''
input_str = "niranjankp"
vowels = "aeiou"
output = {}

for char in input_str:
    if char in vowels and char not in output:
        value = input_str.count(char)
        output[char] = value
print(output)
