# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
# Note:
#
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].


def floodFill(image, sr, sc, newColor):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type newColor: int
    :rtype: List[List[int]]
    """

    # We will use DFS to solve it
    # Create an array similar to the image array with all elements initialized
    # to False

    visited_arr = [[False for _ in range(len(image[0]))] for _ in range(len(image))]

    # Create a stack
    stack = [(sr, sc)]
    visited_arr[sr][sc] = True
    orig_val = image[sr][sc]

    while stack:

        top = stack[-1]

        # Pop this node
        stack.pop()

        r = top[0]
        c = top[1]

        # Mark this node with new color
        image[r][c] = newColor

        # Check all teh elements that are 4-directionally connected to this
        # "top" node

        # need to check the boundaries here
        if 0 < c < len(image[0]) - 1:
            # Need to check the left col and the right column
            if image[r][c+1] == orig_val and not visited_arr[r][c+1]:
                stack.append((r, c+1))
                visited_arr[r][c+1] = True

            if image[r][c-1] == orig_val and not visited_arr[r][c-1]:
                stack.append((r, c - 1))
                visited_arr[r][c - 1] = True

        if c == 0:
            # Need to check only the right column
            if image[r][c+1] == orig_val and not visited_arr[r][c+1]:
                stack.append((r, c+1))
                visited_arr[r][c+1] = True

        if c == len(image[0]) - 1:
            # need to check only the left column
            if image[r][c-1] == orig_val and not visited_arr[r][c-1]:
                stack.append((r, c-1))
                visited_arr[r][c - 1] = True


        # Now the rows
        if 0 < r < len(image) - 1:
            # Need to check the left col and the right column
            if image[r+1][c] == orig_val and not visited_arr[r+1][c]:
                stack.append((r+1, c))
                visited_arr[r + 1][c] = True

            if image[r-1][c] == orig_val and not visited_arr[r - 1][c]:
                stack.append((r - 1, c))
                visited_arr[r - 1][c] = True

        if r == 0:
            # Need to check only the bottom rows
            if image[r+1][c] == orig_val and not visited_arr[r+1][c]:
                stack.append((r + 1, c))
                visited_arr[r + 1][c] = True

        if r == len(image) - 1:
            # need to check only the top rows
            if image[r - 1][c] == orig_val and not visited_arr[r - 1][c]:
                stack.append((r - 1, c))
                visited_arr[r - 1][c] = True

    return image


# Recursive SOlution from https://leetcode.com/problems/flood-fill/solution/
def floodFill_recursive(image, sr, sc, newColor):
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor:
        return image
    dfs(sr, sc)
    return image

def dfs(r, c):
    if image[r][c] == color:
        image[r][c] = newColor
        if r >= 1:
            dfs(r-1, c)
        if r+1 < R:
            dfs(r+1, c)
        if c >= 1:
            dfs(r, c-1)
        if c+1 < C:
            dfs(r, c+1)


# Examples
x = [[1,1,1],[1,1,0],[1,0,1]]
new_color = 2
sr = 1
sc = 1

print("The result is ", floodFill(x, sr, sc, new_color))
