# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.
#

def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    # Credits -> https://leetcode.com/problems/isomorphic-strings/discuss/144556/Python:-Simple-to-understand-solution

    if s == t:
        return True

    return getUniqueList(s) == getUniqueList(t) 

def getUniqueList(s):
    """
    Helper function
    """

    d = {}
    l = []

    for i in range(len(s)):
        ch = s[i]

        if ch not in d:
            # Create a new entry in teh dictionary
            d[ch] = i
            l.append(i)
        else:
            l.append(d[ch])

    return l

s = "egg"
t = "add"

s1 = "foo"
t1 = "bar"
print(isIsomorphic(s1, t1))
