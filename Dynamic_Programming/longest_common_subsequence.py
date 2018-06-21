# Longest Common Subsequence
# Given two sequences, find the length of longest subsequence present in both of them.

# Examples:
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


###########################


def longest_common_subsequence(X, Y):
    """
    Given 2 strings X and Y, this function returns teh length of
    the longest common subsequence of teh 2 strings X, Y

    Example:
    LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
    LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

    Output: int

    ITERATIVE APPROACH
    BOTTOM UP APPROACH
    """
    m = len(X)
    n = len(Y)
    # Create a 2D array to store teh results
    L = [[None] * (n + 1) for i in range(m+1)]

    # Iterate through both teh strings
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]




# Examples

X = "ABCDEFGHIJKL"
Y = "IJKL"


print("The lenght of LCS is ", longest_common_subsequence(X,Y))
