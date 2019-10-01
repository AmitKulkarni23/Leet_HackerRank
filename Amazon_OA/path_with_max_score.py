# Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0]
# and ending at [r - 1, c - 1]. The score of a path is the minimum value in that path. For example,
# the score of the path 8 → 4 → 5 → 9 is 4.
#
# You can only move either down or right at any point in time.
#
# Example 1:
#
# Input:
# [[5, 1],
#  [4, 5]]
# Output: 4
# Explanation:
# Possible paths:
# 5 → 1 → 5 => min value is 1
# 5 → 4 → 5 => min value is 4
# Return the max value among minimum values => max(4, 1) = 4.

# https://leetcode.com/discuss/interview-question/383669/
# Solution https://leetcode.com/playground/6AzPSKy2

# Approach
# Iterate over first row and column. The minimum value must be propagated all the way down the line.
# Each of the internals of the grid will be the minimum of
# 1) itself
# 2) element above it in the grid
# 3) element to the left of it in the grid

# Choose maximum of the 3 comparisons above

# Return grid[-1][-1]

# Time -> O(rows * cols)
# Space -> O(1)


def mmPath(grid):
    if len(grid) == 0:
        return 0

    for i in range(1, len(grid[0])):
        grid[0][i] = min(grid[0][i], grid[0][i - 1])

    for j in range(1, len(grid)):
        grid[j][0] = min(grid[j][0], grid[j - 1][0])

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] = max(min(grid[i][j], grid[i - 1][j]), min(grid[i][j], grid[i][j - 1]))

    return grid[-1][-1]


print(mmPath([[5, 1], [4, 5]]))
print(mmPath([[5, 1, 7], [4, 8, 5]]))
print(mmPath([[1, 9, 9], [9, 9, 9], [9, 9, 9]]))
print(mmPath([[10, 7, 3], [12, 11, 9], [1, 2, 8]]))
print(mmPath([[20, 20, 3], [20, 3, 20], [3, 20, 20]]))