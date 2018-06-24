# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

#########################################################

def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m = len(word1)
    n = len(word2)

    if m == 0:
        # Inster all the characters present in word2
        return n

    if n == 0:
        # Delete all the characters from word1
        return m

    # Create a temporary array
    cache = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            # The first string is empty
            if i == 0:
                cache[i][j] = j

            elif j == 0:
                cache[i][j] = i

            elif word1[i-1] == word2[j -1]:
                cache[i][j] = cache[i-1][j-1]

            else:
                cache[i][j] = 1 + min(cache[i][j-1], cache[i-1][j], cache[i-1][j-1])

    return cache[m][n]

word1 = "intention"
word2 = "execution"

print(minDistance(word1, word2))
