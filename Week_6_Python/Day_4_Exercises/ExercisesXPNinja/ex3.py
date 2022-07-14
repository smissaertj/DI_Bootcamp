"""
Exercise 3: Working On A Paragraph
Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
Paste it to your code, and store it in a variable.
Let’s analyze the paragraph. Print out a nicely formatted message saying:
How many characters it contains (this one is easy…).
How many sentences it contains.
How many words it contains.
How many unique words it contains.
Bonus: How many non-whitespace characters it contains.
Bonus: The average amount of words per sentence in the paragraph.
Bonus: the amount of non-unique words in the paragraph.
"""

import re

text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard
 dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen
 book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially 
unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and
 more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

chars = len(text)
end_of_sentence_mark = '.?!'
sentences = re.split(r'[.?!]', text)
sentences = len(list(filter(None, sentences)))
word_list = list(map(str.strip, text.split(' ')))
word_count = len(word_list)
unique_words = len(set(word_list))
non_unique_words = word_count - unique_words

print(f'Text contains:\n{chars} characters.\n{sentences} sentences.\n{word_count} words.\n{unique_words} unique words\n{non_unique_words} non unique words.')