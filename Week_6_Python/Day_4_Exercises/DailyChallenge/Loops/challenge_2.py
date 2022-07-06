word = input('Provide a word containing duplicate letters: ')
word_list = list(word)

for char in word_list:
    if word_list.count(char) > 1:
        word_list.remove(char)
else:
    print(''.join(word_list))