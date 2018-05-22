# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
#
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
#
#
# Example 1:
#
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: True
# Explanation:
# 1234
# 5123
# 9512
#
# In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
# Example 2:
#
# Input: matrix = [[1,2],[2,2]]
# Output: False
# Explanation:
# The diagonal "[1, 2]" has different elements.
# Note:
#
# matrix will be a 2D array of integers.
# matrix will have a number of rows and columns in range [1, 20].
# matrix[i][j] will be integers in range [0, 99].

def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    # Credits : https://leetcode.com/problems/toeplitz-matrix/solution/

    # What makes 2 co-ordinates( (r1, c1), (r2, c2)) belong on the diagonal
    # It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2


    my_dict = {}

    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if r - c not in my_dict:
                my_dict[r-c] = val
            elif my_dict[r - c] != val:
                return False
    return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(isToeplitzMatrix(matrix))
