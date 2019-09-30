# https://leetcode.com/problems/most-common-word/
# Time -> O(P + B)
# Space -> O(P + B)

# where P is the size of paragraph and B is the size of banned
import collections
import re

# Leetcode Solution -> https://leetcode.com/problems/most-common-word/solution/
def mostCommonWord(paragraph, banned):
    banset = set(banned)
    for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
    count = collections.Counter(
        word for word in paragraph.lower().split())

    ans, best = '', 0
    for word in count:
        if count[word] > best and word not in banset:
            ans, best = word, count[word]

    return ans


# My solution -> 
# def mostCommonWord(paragraph, banned):
#     """
#     :type paragraph: str
#     :type banned: List[str]
#     :rtype: str
#     """
#     # Strip the given string of all the punctuation marks
#     paragraph = re.sub(r'[^\w\s]', '', paragraph)
#
#     # Create a list of valid words
#     valids = [x.lower() for x in paragraph.split() if x.lower() not in banned]
#
#     # collections.Counter(valids).most_common() -> returns a list of tuples
#     # [('ball', 2), ('bob', 1), ('a', 1), ('the', 1), ('flew', 1), ('far', 1), ('after', 1), ('it', 1), ('was', 1)]
#     return collections.Counter(valids).most_common()[0][0]