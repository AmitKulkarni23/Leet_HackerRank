# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# Example:
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    # Credits -> https://www.youtube.com/watch?v=g8bSdXCG-lA
    # Idea -> Use are under histogram for each row in the 2D matrix
    # Use Dynamic programming too create a new 1D array of size = # cols in matrix
    # this array is update column wise for each rows as follows:
    # for i, ele in enumerate(row[j]):
        # if ele == 0:
        #     1d_arr[i] = 0
        # else:
        #     1d_arr[i] += ele


    cols = len(matrix[0])

    # Copy the first row into this new_array
    new_arr = convert_str_to_int_arr(matrix[0])

    # Now calculate the area under the histogram for this list
    max_area = largestRectangleArea(new_arr)

    for i in range(1, len(matrix)):
        update_new_arr(new_arr, convert_str_to_int_arr(matrix[i]))
        area = largestRectangleArea(new_arr)

        if area > max_area:
            max_area = area


    return max_area

def convert_str_to_int_arr(arr):
    """
    Helper function which converts a string array to an int array
    """
    int_arr = [0] * len(arr)

    for i in range(len(arr)):
        int_arr[i] = int(arr[i])

    return int_arr

def update_new_arr(new_arr, row_arr):
    """
    Helper function to update the new array according the logic below
    """

    for i, ele in enumerate(row_arr):
        if ele == 0:
            new_arr[i] = 0
        else:
            new_arr[i] += ele


def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    # Credits -> https://www.youtube.com/watch?v=ZmnqCZp9bBs

    # Initialize max_area and area
    max_area = 0
    area = 0

    stack = []
    i = 0
    while i < len(heights):
        if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
            # Step 1 from algorithm
            # Push teh current index to stack
            # print("i going in first if statement", i)
            stack.append(i)
            i += 1
        else:
            # keep removing elements unitl we find a value lesser
            # than the current value
            top = stack.pop()
            # Check if stack is empty
            if not stack:
                area = heights[top] * i
            else:
                area = heights[top] * ( i - stack[-1] -1)
            # Compare with max area
            if area > max_area:
                max_area = area

    while len(stack):
        top = stack.pop()
        if not stack:
            area = heights[top] * i
        else:
            area = heights[top] * ( i - stack[-1] -1)

        if area > max_area:
            max_area = area


    return max_area


matrix = [
  ["1","0","0","1","1","1"],
  ["1","0","1","1","0","1"],
  ["0","1","1","1","1","1"],
  ["0","0","1","1","1","1"]
]



print(maximalRectangle(matrix))
