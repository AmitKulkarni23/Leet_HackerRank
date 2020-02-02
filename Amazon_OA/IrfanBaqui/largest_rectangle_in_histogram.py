# Given an array with integers representing the heights of bars in a histogram,
# calculate the area of the largest rectangle in the histogram.

def max_area(hist):
    stack = []
    rect_area = 0
    idx = 0

    while idx < len(hist):
        # Push the index into the stack on 2 conditions
        if not stack or hist[stack[-1]] <= hist[idx]:
            stack.append(idx)
            idx += 1
        else:
            # At this point, we are at a bar that is of the highest length
            # amongst the bars that are in the stack
            # Note: In the if branch we did an idx += 1

            cur_max_bar = hist[stack.pop()]

            # How many steps do we move left
            left = (idx - 1 - stack[-1]) if len(stack) else (idx - 1)

            area = cur_max_bar * left # height * width
            rect_area = max(rect_area, area)

    while stack:
        # This is for the reamining bars that we haven't yet computed
        # the area for

        # Same logic as above
        # Note: In the if branch we did an idx += 1

        cur_max_bar = hist[stack.pop()]

        # How many steps do we move left
        left = (idx - 1 - stack[-1]) if len(stack) else (idx - 1)

        area = cur_max_bar * left # height * width
        rect_area = max(rect_area, area)


    return rect_area

hist = [1, 2, 3, 4, 5, 3, 3, 2]
print(max_area(hist))
