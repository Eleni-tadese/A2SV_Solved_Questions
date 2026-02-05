from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):

        char_dict = Counter(chars)
        lengths = 0
        for word in words:
            word_dict = Counter(word)
            if not (word_dict - char_dict):
                lengths += len(word)

        return lengths