# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    # Credits -> https://leetcode.com/problems/triangle/discuss/38724/7-lines-neat-Java-Solution
    if not triangle:
        # there are no elements in teh triangle
        return None

    # DP solution
    t_len = len(triangle)

    # Create a 1d array
    a = [0 for _ in range(t_len + 1)]

    for i in range(t_len - 1, -1, -1):
        for j in range(len(triangle[i])):
            a[j] = min(a[j], a[j+1]) + triangle[i][j]

    # print(a)
    return a[0]
# Examples
matrix = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3],
  [11,12, 13, 14, 15]]

print(minimumTotal(matrix))
