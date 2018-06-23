# Python Program illustrating edit distance
# Given two strings str1 and str2 and below operations that can performed on
# str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

# Insert
# Remove
# Replace
# Input:   str1 = "geek", str2 = "gesek"
# Output:  1
# We can convert str1 into str2 by inserting a 's'.
#
# Input:   str1 = "cat", str2 = "cut"
# Output:  1
# We can convert str1 into str2 by replacing 'a' with 'u'.
#
# Input:   str1 = "sunday", str2 = "saturday"
# Output:  3
# Last three and first characters are same.  We basically
# need to convert "un" to "atur".  This can be done using
# below three operations.
# Replace 'n' with 'r', insert t, insert a


def edit_distance(S1, S2, m, n):
    """
    Function that determines the minimum number of operations required to
    convert string S1 to S2

    m = len(S1)
    n = len(S2)

    Time Complexity: O(3 ^ m)
    """
    if m == 0:
        # Then we need to insert all characters of 2nd string into teh first
        # string
        return n

    if n == 0:
        # Then remove all charcters of the 1st string
        return m

    # Now, if teh last 2 characters of both teh strings are equal then
    # we have recur with m -1, n -1 characters
    if S1[m-1] == S2[n-1]:
        return edit_distance(S1, S2, m-1, n-1)

    # Else:
    # There are 3 options
    # Insert: If you insert a character into S1, then we have to recur
    # for m and n -1 characters
    # Remove: REmoving a character from S1( to make S1 == S2), then recur
    # for m -1 and n -1 characters
    # Replace: Replace a character in S1 with a character then recur for m -1 and
    # n - 1 characters
    # Take teh minimum f these three operations

    return 1 + min(edit_distance(S1, S2, m, n - 1),
                    edit_distance(S1, S2, m - 1, n),
                    edit_distance(S1, S2, m - 1, n - 1))


def edit_distance_memoized(S1, S2, m, n):
    """
    Function to calculate the minimumm edit distance between S1 and S2
    The same as above

    Time COmplexity: O(m * n)
    Use a temporary array

    Credits: https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
    """

    # Create a temporary arrayof size (m + 1) * ( n + 1)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Iterate through both teh strings
    for i in range(m + 1):
        for j in range(n + 1):

            # If teh first string is empty, insert all characters of S2 into S1
            if i == 0:
                dp[i][j] = j

            # Similary if second string is empty, we have to remove all characters
            # from S1
            elif j == 0:
                dp[i][j] = i


            # Else do all teh oeprations
            # Check if teh last 2 character strings are equal
            elif S1[i - 1] == S2[j -1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i][j-1],
                                    dp[i-1][j],
                                    dp[i-1][j-1])

    print(dp)
    return dp[m][n]

# Examples:
s1 = "cat"
s2 = "cut"
print(edit_distance_memoized(s1, s2, len(s1), len(s2)))
