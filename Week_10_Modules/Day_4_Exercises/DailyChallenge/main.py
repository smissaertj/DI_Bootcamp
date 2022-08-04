class Text:
    def __init__(self, string):
        self.string = string.lower()

    def frequency(self, word):
        """ return the frequency of a word in the text """
        return self.string.count(word.lower()) if self.string.count(word.lower()) > 0 else 'Word not found in sentence.'

    def most_common(self):
        """ return the most common word in the text """
        count = {}
        for word in self.string.split(' '):
            count[word.lower()] = self.string.count(word)
        sorted_count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}
        return list(sorted_count)[-1]

    def unique_words(self):
        """ return a list of all the unique words """
        return [word for word in self.string.split() if self.string.split().count(word) == 1]


my_text = Text('A good book would sometimes cost as much as a good house')
print(my_text.frequency('a'))
print(my_text.most_common())
print(my_text.unique_words())


the_stranger = None
with open('the_stranger.txt', mode='r') as file:
    the_stranger = Text(file.read())

print(the_stranger.frequency('the'))
print(the_stranger.most_common())
print(the_stranger.unique_words())
