# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.
#
# For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
#
# Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.
#
# However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
#
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.
#
# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
#
# Note:
#
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].

def areSentencesSimilar(self, words1, words2, pairs):
    """
    :type words1: List[str]
    :type words2: List[str]
    :type pairs: List[List[str]]
    :rtype: bool
    """

    # Credits -> https://leetcode.com/problems/sentence-similarity/solution/

    # Cases
    # if length of both the lists are not same
    if len(words1) != len(words2):
        return False

    # If both lists are same, return True
    if words1 == words2:
        return True

    # Algorithm
    # Check if words1[i] == words2[i]
    # Or Check if (words1[i], words2[i]) appear in pairs
    # or check if (words2[i], words1[i]) appera in pairs

    # Create a set
    pair_set = set(map(tuple, pairs))

    return all(w1 == w2 or (w1, w2) in pair_set or (w2, w1) in pair_set for w1, w2 in zip(words1, words2))
