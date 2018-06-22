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

    Time Complexity - O(mn)

    Example:
    LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
    LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

    Output: int

    ITERATIVE APPROACH
    BOTTOM UP APPROACH
    """
    m = len(X)
    n = len(Y)
    # Create a 2D array to store teh results of size (n + 1) x (m + 1)
    L = [[None] * (n + 1) for i in range(m+1)]

    print(L)

    # Iterate through both teh strings
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    print("After everything L is ")
    print(L)

    return L[m][n]


def recursive_LCS(X, m, Y, n):
    """
    Recursive implementation of teh LCS problem
    Time Complexity - O( 2 ^ n)
    Inputs:
    X - string
    m - len(X)
    Y - string
    n - len(Y)
    """

    # Base Case
    # If the lenght of either of teh strings is 0, return 0

    if m == 0 or n == 0:
        return 0

    # Else, check the last characters of both teh strings
    if X[m - 1] == Y[n - 1]:
        # If teh last characters match
        return 1 + recursive_LCS(X, m-1, Y, n-1)
    else:
        # Teh last characters do not match
        return max(recursive_LCS(X, m, Y, n-1), recursive_LCS(X, m - 1, Y, n))


# Examples

X = "AJK"
Y = "IJK"


# print("The lenght of LCS is ", longest_common_subsequence(X,Y))
print("Recursive LCS ", recursive_LCS(X, len(X), Y, len(Y)))
