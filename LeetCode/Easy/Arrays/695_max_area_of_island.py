# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # Use DFS
    # Time Complexity O(R * C)
    # Space Complexity O(R * C)

    # Mark a node as visited each time we visit it
    # Credits -> https://leetcode.com/problems/max-area-of-island/solution/

    seen = set()

    area = 0

    for i, r_val in enumerate(grid):
        for j, c_val in enumerate(r_val):

            if c_val and (i, j) not in seen:

                # Add it to seen set
                seen.add((i, j))
                shape = 0
                stack = [(i, j)]

                # Now apply actual DFS
                while stack:
                    r, c = stack.pop()
                    shape += 1
                    # Check the neighbours
                    for x, y in ((r - 1, c), (r+1, c),(r, c-1), (r, c+1)):
                        # Check if the value is 1
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and (x, y) not in seen:
                            # Add this stack and seen
                            stack.append((x, y))
                            seen.add((x, y))


                # Take the max area
                area = max(area, shape)

        return area
