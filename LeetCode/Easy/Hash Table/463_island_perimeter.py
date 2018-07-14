# You are given a map in form of a two-dimensional integer grid where 1 represents
# land and 0 represents water. Grid cells are connected horizontally/vertically
# (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

#
# Example:
#
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Answer: 16

def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # Idea -. Count the number o edges adjacent to water

    rows = len(grid)
    cols = len(grid[0])

    per = 0

    # Count the number of edges adjacent to the water
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    per += 1
                if j == 0 or grid[i][j-1] == 0:
                    per += 1

                if i == rows - 1 or grid[i+1][j] == 0:
                    per += 1
                if j == cols - 1 or grid[i][j+1] == 0:
                    per += 1

    return per
