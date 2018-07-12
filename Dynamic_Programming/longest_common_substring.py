# Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
#
# Examples :
#
# Input : X = "GeeksforGeeks", y = "GeeksQuiz"
# Output : 5
# The longest common substring is "Geeks" and is of
# length 5.
#
# Input : X = "abcdxyz", y = "xyzabcd"
# Output : 4
# The longest common substring is "abcd" and is of
# length 4.

# The longest common suffix has following optimal substructure property
#    LCSuff(X, Y, m, n) = LCSuff(X, Y, m-1, n-1) + 1 if X[m-1] = Y[n-1]
#                         0  Otherwise (if X[m-1] != Y[n-1])
#
# The maximum length Longest Common Suffix is the longest common substring.
#    LCSubStr(X, Y, m, n)  = Max(LCSuff(X, Y, i, j)) where 1 <= i <= m
#                                                      and 1 <= j <= n


# Credits -> https://www.geeksforgeeks.org/longest-common-substring/

# m = len(x)
# n = len(Y)
# Time Complexity -> O(m*n)
# Space Complexity -> O(m+1 * n+1)


def longest_common_substring(X, Y):
    """
    Function that returns the longets common substring
    """

    # Solving it using Dynamic programming

    m = len(X)
    n = len(Y)

    # Create a cache

    cache = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    max_len = 0

    # Iterate through the string to store the lenght of the largest common suffix in the
    # cache
    for i in range(m+1):
        for j in range(n+1):

            if i == 0 or j == 0:
                cache[i][j] = 0

            elif X[i - 1] == Y[j - 1]:
                cache[i][j] = cache[i-1][j-1] + 1
                max_len = max(cache[i][j], max_len)

            else:
                cache[i][j] = 0

    return max_len


# Examples:
# X = "abcdxyz"
# Y = "xyzabcd"

X = "zxabcdezy"
Y = "yzabcdezx"

print("LCS is ", longest_common_substring(X, Y))
