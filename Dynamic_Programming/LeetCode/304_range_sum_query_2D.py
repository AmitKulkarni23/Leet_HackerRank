# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
#
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

import pprint
class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # Credits -> https://leetcode.com/problems/range-sum-query-2d-immutable/solution/
        
        if not matrix:
            # If there are no elements in the matrix
            return None

        if not matrix[0]:
            # If the matrix rows / columns are empty
            return

        rows = len(matrix)
        cols = len(matrix[0])

        # Create a 2 dimesnion cache
        self.dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        # Now iterate through the array and store the results in the cache
        for i in range(rows):
            for j in range(cols):
                self.dp[i + 1][j + 1] = self.dp[i+1][j] + self.dp[i][j+1] + matrix[i][j] - self.dp[i][j]


        # pprint.pprint(dp)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # Consider O as origin
        # sum(ABCD) = sum(OD) - sum(OC) - sum(OB) + sum(OA)
        # Why + sum(OA) -> because sum(OA) is subtracted twice
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

num_mat = NumMatrix(matrix)
print(num_mat.sumRegion(2,1, 4, 3))
