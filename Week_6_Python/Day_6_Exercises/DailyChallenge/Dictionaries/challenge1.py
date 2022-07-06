"""
Challenge 1
Ask a user for a word
Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

Make sure the letters are the keys.
Make sure the letters are strings.
Make sure the indexes are stored in a list and those lists are values.
"""

word = input('Provide any word: ')
word_list = [char for char in word]
print(word_list)

word_dict = {}

position = 0
for char in word_list:
    if word_dict.get(char):
        word_dict[char].append(word_list.index(char, position))
    else:
        word_dict[char] = list(str(word_list.index(char, position)))
    position += 1
else:
    print(word_dict)