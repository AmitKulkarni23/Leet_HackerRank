# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Example 1:
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
#
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# Example 2:
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
#
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^

# Time Complexity : O(n ^ 2)
# Space Complexity : O( n ^ 2)

import pprint
def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    # Explanation Credits -> https://www.youtube.com/watch?v=InjW43eRq5I&t=1097s

    s_len = len(s)
    t_len = len(t)

    # Corner Cases
    if s_len == 0 or t_len == 0:
        return 0

    # Create a 2D array of size s+1 x t+1
    cache = [[0 for i in range(t_len+1)] for _ in range(s_len+1)]


    # Fill the first column in the array with 1s
    for i in range(s_len + 1):
        cache[i][0] = 1


    # Now iterate through teh strings and fill the cache
    for i in range(1, s_len+1):
        for j in range(1, t_len+1):
            if s[i - 1] == t[j - 1]:
                # It is a match
                cache[i][j] = cache[i-1][j-1] + cache[i-1][j]

            else:
                # No match
                cache[i][j] = cache[i-1][j]

    # pprint.pprint(cache)

    return cache[-1][-1]


# Examples:
# S = "rabbbit"
# T = "rabbit"

S = "babgbag"
T = "bag"
print(numDistinct(S, T))
