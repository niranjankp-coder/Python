# Find Longest Word
sentence = "NVMe SSD Storage Validation"

longest_word = ""
data = sentence.split()
for word in data:
  if len(word) > len(longest_word):
    longest_word = word
print(f"longest word in the sentence is: \"{longest_word}\"")

'''
output:
longest word in the sentence is: "Validation"
'''
