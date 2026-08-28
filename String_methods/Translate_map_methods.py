# maketrans() + translate()
# Replace characters using mapping

# Replace vowels with *
text = "Hello World"
table = str.maketrans("aeiou", "*****")
print(text.translate(table))   # "H*ll* W*rld"

# Delete characters
table2 = str.maketrans("", "", "aeiou")
print(text.translate(table2))  # "Hll Wrld"

# expandtabs() - Replace \t with spaces
text2 = "Hello\tWorld"
print(text2.expandtabs(4))     # "Hello   World"
print(text2.expandtabs(10))    # "Hello     World"
