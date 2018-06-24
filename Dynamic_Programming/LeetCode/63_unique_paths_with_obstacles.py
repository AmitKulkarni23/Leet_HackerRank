# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right


#########################################


def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int

    """

    # Credits -> https://leetcode.com/problems/unique-paths-ii/discuss/140450/36ms-Python3-DP-solution
    #
    # Similar to whatever we had seen for coin change problem
    # To caclulate F(i) -> we should know all F(x) where x < i


    # handle corner cases
    if not obstacleGrid or not obstacleGrid[0]:
        return 0

    if obstacleGrid[0][0] == 1:
        # The first cell itself is an obstacle, the robot cannot move forward
        # Therefore 0 unique paths
        return 0

    # Get the dimensions first
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    # Create a cache
    cache = [0 for _ in range(m)]
    # print(cache)
    cache[0] = 1

    for i in range(n):
        for j in range(m):
            if obstacleGrid[j][i] == 1:
                cache[j] = 0
                continue

            if j == 0:
                continue

            cache[j] += cache[j-1]

        # print(cache)
    return cache[-1]
# Examples:
obg = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

print(uniquePathsWithObstacles(obg))
