# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    # Credits -> https://leetcode.com/problems/number-of-islands/solution/

    # Treat the 2d grid map as an undirected graph and
    # there is an edge between two horizontally or vertically adjacent nodes of value '1'.

    # Linear scan the 2d grid map, if a node contains a '1',
    # then it is a root node that triggers a Depth First Search.
    # During DFS, every visited node should be set as '0' to mark as visited node.
    # Count the number of root nodes that trigger DFS,
    # this number would be the number of islands since each DFS starting
    # at some root identifies an island.

    num_rows = len(grid)
    if not num_rows:
        # There are no islands
        return 0

    num_cols = len(grid[0])

    total_num_islands = 0

    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == "1":
                total_num_islands += 1
                dfs(grid, r, c)

    return total_num_islands

def dfs(grid, r, c):
    """
    Helper function which performs dfs search
    """
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Mark the node at grid[r][c] as visited
    grid[r][c] = "0"

    if r - 1 >= 0 and grid[r-1][c] == "1":
        dfs(grid, r - 1, c)

    if r + 1 < num_rows and grid[r + 1][c] == "1":
        dfs(grid, r + 1, c)

    if c - 1 >= 0 and grid[r][c - 1] == "1":
        dfs(grid, r, c - 1)

    if c + 1 < num_cols and grid[r][c + 1] == "1":
        dfs(grid, r, c + 1)
