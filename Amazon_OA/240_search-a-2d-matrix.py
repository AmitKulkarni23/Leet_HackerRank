# https://leetcode.com/problems/search-a-2d-matrix-ii/

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # Credits -> https://leetcode.com/problems/search-a-2d-matrix-ii/solution/
    # Time Complexity -> O(m + n)
    # Space = O(1)

    # Algorithm:
    # Start from the bottom left corner
    # If current value > target:
    #   row--
    # If current value < target:
    #   col++
    # if current_Value == target:
    #   return True
    # if the current_Value is out of bounds:
    # return False

    row = len(matrix) - 1
    col = 0

    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
        else:
            return True

    return False

