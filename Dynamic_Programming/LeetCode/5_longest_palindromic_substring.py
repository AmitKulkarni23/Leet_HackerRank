# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

import pprint
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    # Refernce -> https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
    # Time Complexity -> O(n^2)
    # Space Complexity -> O(n^2)
    n = len(s)

    if not n:
        return ""

    table = [[False for _ in range(n)] for _ in range(n)]

    # All substrings of lenght 1 are palindromes
    # Therefore table[i][i] -> true

    # max-len -> stores the lenght of the palindromic substring
    max_len = 1
    for i in range(n):
        table[i][i] = True

    # Check for substrings of len = 2
    # strat -> stores the starting index of the substring
    start = 0
    for i in range(n - 1):
        if s[i] == s[i+1]:
            table[i][i+1] = True
            start = i
            max_len = 2


    # For substrings of lenght greater than 2
    # k - represents lenght of the substring we are currently checking
    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i + k - 1

            # Check if table[i+1][j-1] is True
            # and str[i] == str[j]
            # This means that adding str[i] and str[j] to the already existing
            # palindrome will give us palindrome

            if table[i+1][j-1] and s[i] == s[j]:
                table[i][j] = True

                if k > max_len:
                    start = i
                    max_len = k

    return s[start:start+max_len]


def best_leetcode_sol(s):
    """
    :type s: str
    :rtype: str
    """

    # mancher Algorithm
    maxLen = 0
    maxStartInd = 0
    for i in range(len(s)):
        if i-maxLen >= 0 and self.isPalindrome(s[i-maxLen:i+1]):
            maxStartInd = i-maxLen
            maxLen += 1
        elif i-maxLen-1 >= 0 and self.isPalindrome(s[i-maxLen-1:i+1]):
            maxStartInd = i-maxLen-1
            maxLen += 2

    return s[maxStartInd:maxStartInd+maxLen]


def isPalindrome(self, s):
    return s == s[::-1]

# Examples:
s = "cbbd"
print(longestPalindrome(s))
