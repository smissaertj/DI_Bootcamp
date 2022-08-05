class AnagramChecker():
    def __init__(self):
        self.word_list = None
        with open('sowpods.txt', mode='r') as file:
            content = file.readlines()
            self.word_list = [word.lower().strip() for word in content]

    def is_valid_word(self, word):
        """ check if a given word is a valid word """
        return True if word.lower() in self.word_list else False

    def get_anagrams(self, user_word):
        """ find all anagrams for the given word """
        anagrams = []
        for word in self.word_list:
            if self.is_anagram(word, user_word.lower()) and word != user_word.lower():
                anagrams.append(word)
        return anagrams if len(anagrams) > 0 else None

    @staticmethod
    def is_anagram(word1, word2):
        """ return True if both words are the same length and contain the same letters """

        # An anagram is always the same length
        if len(word1) == len(word2):
            for letter in word1.lower():
                # Check if all the letters in word1 are also in word 2
                if letter not in word2.lower():
                    return False # as soon as we have 1 letter that is not in word2, we do not have an anagram

                # Inverse check: For each letter we have in word1, check if all the letters in word2 are in word1.
                for letter in word2.lower():
                    if letter not in word1.lower():
                        return False
            else:
                return True # If the for loop never returned False (and break the loop), then we have an Anagram.
        else:
            return False
