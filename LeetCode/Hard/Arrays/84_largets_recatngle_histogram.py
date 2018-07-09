# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
# Example:
#
# Input: [2,1,5,6,2,3]
# Output: 10


# Idea: Use a stack
# Algorithm

# -> add an index i to stack if input[i] >= top of stack
# -> else remove elements from stack till a number which is smaller or equal is found
# -> If stack is ewmpty:
    # area = input[top] * i
    # max_area = max(max_area, area)
# else:
    # area = input[top] * (i - stack.top -1)
    # max_area = max(area, max_area)

# return max_area


def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
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
            # print("Stack is ", stack)
        else:
            # keep removing elements unitl we find a value lesser
            # than the current value
            # print("Coming into the else loop", i)
            top = stack.pop()
            # print("Top is ", top)
            # Check if stack is empty
            if not stack:
                area = heights[top] * i
                # print("Area contribution when stack is empty by ", i , "is ", area)
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

# heights = [1,2,4]
# heights = [2,1,2,3,1]
heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))
