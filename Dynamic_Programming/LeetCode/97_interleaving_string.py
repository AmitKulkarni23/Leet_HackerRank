# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# Example 1:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

# Time Complexity : O(m . n)
# where m = len(s1)
# and n = len(s2)
#
# we need to fill the cache
#
# Space Complexity O((m+1) * (n+1))

import pprint
def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """

    s1_len = len(s1)
    s2_len = len(s2)

    s3_len = len(s3)

    if s3_len != s1_len + s2_len:
        return False

    # Create the 2d matrix which will act as our cache
    cache = [[False for _ in range(s1_len + 1)] for _ in range(s2_len + 1)]

    # Now initilaize the 1st row and 1st column in the array
    cache[0][0] = True

    # Initilaize the first row
    for i in range(1, s1_len+1):
        if s3[i - 1] == s1[i-1]:
            # then make the matrix element as True
            cache[0][i] = cache[0][i-1]

    # Similarly initialize the first column
    for j in range(1, s2_len+1):
        if s3[j-1] == s2[j-1]:
            # Then make cache[j] = True
            cache[j][0] = cache[j-1][0]

    # Now iterate through the characters in s3
    for i in range(1, len(cache)):
        for j in range(1, len(cache[i])):
            l = i + j - 1

            # Need to check special case where both the strings are equal
            if s2[i - 1] == s3[l] and s1[j-1] == s3[l]:
                if cache[i-1][j]:
                    cache[i][j] = True

                elif cache[i][j-1]:
                    cache[i][j] = True

                continue


            # Check against s1
            if s2[i - 1] == s3[l] or s1[j-1] == s3[l]:
                if s2[i-1] == s3[l]:
                    cache[i][j] = cache[i-1][j]
                else:
                    cache[i][j] = cache[i][j-1]

    # pprint.pprint(cache)
    return cache[-1][-1]

s1 = "aabc"
s2 = "abad"
s3 = "aabadabc"

# s1 = "ab"
# s2 = "bc"
# s3 = "babc"

print(isInterleave(s1, s2, s3))
