# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/description/

class Solution:
    def countValidWords(self, sentence: str) -> int:
        valid_words = 0
        for word in sentence.split():
            if self.is_valid_word(word):
                valid_words += 1
        return valid_words

    def is_valid_word(self, word: str) -> bool:
        hyphens = 0
        punctuations = 0

        for i, ch in enumerate(word):
            if ch.isdigit():
                return False

            if ch == '-':
                hyphens += 1
                # at most one hyphen, and must be surrounded by letters
                if (hyphens > 1
                    or i == 0
                    or i == len(word) - 1
                    or not (word[i-1].islower() and word[i+1].islower())):
                    return False

            if ch in "!.,":
                punctuations += 1
                # at most one punctuation, and only at end
                if punctuations > 1 or i != len(word) - 1:
                    return False

            # any other character must be a lowercase letter
            if not (ch.islower() or ch in "-!.," or ch.isdigit() == False):
                return False

        return True
