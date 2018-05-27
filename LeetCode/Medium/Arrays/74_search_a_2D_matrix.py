# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    # Corner conditions
    if target < matrix[0][0]:
        return False

    mat_len = len(matrix) - 1
    if target > matrix[mat_len][-1]:
        return False

    # Since the numbers are sorted in each row
    # finally we have to do a binary search once we find out which row to search in
    # Check out helper function binary_search_helper
    for row in matrix:
        if target <= row[-1]:
            return binary_search_helper(row, 0, len(row) - 1, target)

    return False


def binary_search_helper(arr, low, high, target):
    """
    Function that performs binary search
    """

    if low <= high:
        mid = ( low + high ) // 2

        if arr[mid] == target:
            return True

        if arr[mid] > target:
            # Search in the left array
            high = mid - 1
            return binary_search_helper(arr, low, high, target)
        else:
            low = mid + 1
            return binary_search_helper(arr, low, high, target)

    return False

# Test Examples:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3


matrix_2 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target_2 = 13
print(searchMatrix(matrix, target))
