# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

#########################################################

# Time 91ms
def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    # We will initilaize a cache first
    m = len(grid)  # Number of rows
    n = len(grid[0]) # Number of columns

    # Corner Cases
    if not grid:
        return 0

    cache = [[0 for _ in range(n)] for _ in range(m)]

    # Initilaize teh first element in teh cache
    cache[0][0] = grid[0][0]

    # print(cache)

    # Similarly initilaize the first column of teh cache matrix
    for i in range(1, m):
        cache[i][0] = cache[i-1][0] + grid[i][0]

    # print("After column initiliazation")
    # print(cache)

    # Initiliaze teh first row of the cache
    for i in range(1, n):
        cache[0][i] = cache[0][i-1] + grid[0][i]

    # print("After row initiliazation")
    # print(cache)

    # Now iterate through the array and fill teh cache matrix
    for i in range(1, m):
        for j in range(1,n):
            cache[i][j] = min(cache[i-1][j], cache[i][j-1]) + grid[i][j]

    # print(cache)
    return cache[-1][-1]

# Uses 1D array instead of 2D array
# Time : 50 ms
def best_leet_code_sol(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])


    if m == 0 or n == 0:
        return 0

    res = [0] + [float("inf")]*(n-1)

    for i in range(m):
        res[0] = res[0] + grid[i][0]
        for j in range(1, n):
            res[j] = min(res[j], res[j-1]) + grid[i][j]

    return res[-1]

# Examples:
input = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]


input_2 = [
    [1, 7, 11],
    [2, 4, 13],
    [1, 1, 2]
]

print(minPathSum(input_2))
