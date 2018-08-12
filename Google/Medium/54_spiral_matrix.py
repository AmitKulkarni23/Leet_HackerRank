# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Credits -> https://leetcode.com/problems/spiral-matrix/solution/
# IDEA: Draw the path that the spiral makes.
# We know that the path should turn clockwise whenever it would go out of
# bounds or into a cell that was previously visited.

def spiralOrder(matrix):
    if not matrix:
        return []

    # Create a seen matrix which has the same number of rows and columsn as the
    # given matrix

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    seen = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    answer = []

    # Maintain 2 lists direction in row and direction in column
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = c = di = 0

    for _ in range(num_cols * num_rows):
        answer.append(matrix[r][c])

        seen[r][c] = True

        cand_r, cand_c = r + dr[di], c + dc[di]

        # Check for out of bounds and seen condition
        if 0 <= cand_r < num_rows and 0 <= cand_c < num_cols and seen[cand_r][cand_c] = False:
            # Then this is our new element
            r, c = cand_r, cand_c
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]

    return answer
