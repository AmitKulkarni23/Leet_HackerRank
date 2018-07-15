# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
# Example 1:
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"
#
# Output: False
# Example 3:
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """

    # Concatenate the given string with iteself
    # Eg: s = "abab"
    # s1 = "abababab"
    # s2 = s1[1:len(s1) - 1]
    # s2 = "bababa"

    # if s in s2:
    #     return True

    s1 = s + s
    s2 = s1[1:len(s1) - 1]

    return s in s2
