# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Example:
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4

import pprint
def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    # Credits -> https://www.youtube.com/watch?v=_Lf1looyJMU

    # Create a 2D cache
    rows = len(matrix)
    cols = len(matrix[0])

    cache = [[0 for _ in range(cols)] for _ in range(rows)]

    max = 0

    # Copy the first row into the cache
    for i in range(len(matrix[0])):
        cache[0][i] = int(matrix[0][i])

        if int(matrix[0][i]) == 1:
            max = 1

    # Copy the 1st column into the cache
    for i in range(len(matrix)):
        cache[i][0] = int(matrix[i][0])

        if int(matrix[i][0]) == 1:
            max = 1


    for i in range(1, rows):
        for j in range(1, cols):
            if int(matrix[i][j]) == 1:
                cache[i][j] = min(cache[i-1][j-1], cache[i-1][j], cache[i][j-1]) + 1

                if cache[i][j] > max:
                    max = cache[i][j]

    return max ** 2

# Examples:
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))
