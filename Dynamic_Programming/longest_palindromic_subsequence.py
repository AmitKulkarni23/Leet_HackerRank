# Given a sequence, find the length of the longest palindromic subsequence in it.

def lps_recursive(str, i , j):
    """
    Function that returns the longest palindromic subsequence in a sequence
    """

    # Base Cases
    if i == j:
        # Means there is only 1 character
        return 1

    # Base Case
    if str[i] == str[j] and j == i + 1:
        # The entire strlen is 2 and both the characters present in teh string are
        # equal
        return 2

    if str[i] == str[j]:
        # The first and teh last characters match
        return lps_recursive(str, i+1, j-1) + 2

    # Else ther is no match
    return max(lps_recursive(str, i+1, j), lps_recursive(str, i, j-1))

def lps_dynamic_programming(str):
    """
    Function that returns the longest palindromic subsequence in a sequence
    """

    n = len(str)

    # Create a 2D matrix called as cache of size n x n
    cache = [[0 for _ in range(n)] for _ in range(n)]

    # The diagonal elements will all be 1
    # Why? -> Because LPS of str where len(str) == 1 is 1

    for i in range(n):
        cache[i][i] = 1


    # Build cache in bottom up manner
    # We do not build teh lower half of teh table since they are not
    # used in any place

    # Credits -> https://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i+ cl -1

            if str[i] == str[j] and cl == 2:
                # Lenght of string is 2 and they are equal
                cache[i][j] = 2
            elif str[i] == str[j]:
                # The last 2 characters are equal
                cache[i][j] = 2 + cache[i+1][j-1]
            else:
                cache[i][j] = max(cache[i][j-1], cache[i+1][j])

    return cache[0][n-1]

# Examples:
str = "bacbca"
n = len(str)
print("The LPS for", str, "is", lps_recursive(str, 0, n - 1))
print("The LPS for", str, "is", lps_dynamic_programming(str))
