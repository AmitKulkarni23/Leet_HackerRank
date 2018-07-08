# Given a matrix A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
#
#
#
# Example 1:
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:
#
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
#
#
# Note:
#
# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000


def transpose(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """

    rows = len(A)
    cols = len(A[0])

    # Create a new matrix of cols x rows
    new_mat = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(cols):
        for j in range(rows):
            new_mat[i][j] = A[j][i]


    return new_mat

a = [[1,2,3],[4,5,6],[7,8,9]]
# b = [[1,2,3],[4,5,6]]
c = [[1]]
transpose(c)
