# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:
#
# a) it                      --> it    (no abbreviation)
#
#      1
#      ↓
# b) d|o|g                   --> d1g
#
#               1    1  1
#      1---5----0----5--8
#      ↓   ↓    ↓    ↓  ↓
# c) i|nternationalizatio|n  --> i18n
#
#               1
#      1---5----0
#      ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
#
# Example:
#
# Given dictionary = [ "deer", "door", "cake", "card" ]
#
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true

class ValidWordAbbr(object):

    # Credits -> https://leetcode.com/problems/unique-word-abbreviation/solution/
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        # Store the given dictionary as an instance variable
        self.dict = dictionary # -> This is a list

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """

        # We need to check 3 conditions
        # Condition 1 -> If the given word is same as the word in
        # dicitonary then the abbrevation will be the same, therefore we need to
        # ignore such a word

        word_len = len(word)

        for item in self.dict:
            item_len = len(item)
            if word == item:
                continue

            # Condition 2 and 3 : If the length of the 2 words are same
            # and the first and last characters of the 2 words are same, then the abbrevation
            # will not be unique

            if word_len == item_len and item[0] == word[0] and item[item_len - 1] == word[word_len -1]:
                # Not an unique abbrevation
                return False


        # If all conditions fail
        return True





# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
