"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    # Time: O(R * C)
    # Space: O(R * C)
    
    if not grid:
        return 0

    def dfs(r, c):
        grid[r][c] = "0"

        for cr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= cr < m and 0 <= cc < n and grid[cr][cc] == "1":
                dfs(cr, cc)


    m = len(grid)
    n = len(grid[0])
    ans = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                ans += 1
                dfs(i, j)

    return ans
