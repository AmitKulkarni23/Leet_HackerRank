# Given a string s and a string t, check if s is subsequence of t.
#
# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
# s = "abc", t = "ahbgdc"
#
# Return true.
#
# Example 2:
# s = "axc", t = "ahbgdc"
#
# Return false.
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

# Runtime -> 138ms
def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    # We traverse through both the strings and compare the characters
    m = len(s)
    n = len(t)

    i, j = 0, 0

    while i < m and j < n:
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == m

# Runtime -> 36ms
def isSubsequence_best_leetcode_sol(s, t):
    # Note : find() returns the index of the first occurence
    # if not found -> returns -1
    for c in s:
        i = t.find(c)
        if i == -1:
            return False
        else:
            t = t[i+1:]
    return True