# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # Credits -> https://www.youtube.com/watch?v=pq7Xon_VXeU
    # Time Complexity -> O(n)
    # Space Complexity -> O(1)
    l , r = 0, len(height) - 1

    left_max, right_max = 0, 0

    ans = 0

    while l < r:
        if height[l] < height[r]:
            if height[l] >= left_max:
                # Update left max
                left_max = height[l]
            else:
                # Update answer
                ans += left_max - height[l]

            l += 1
        else:
            if height[r] >= right_max:
                # Update right max
                right_max = height[r]
            else:
                # Update answer
                ans += right_max - height[r]

            r -= 1

    return ans

# Examples:
input = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(input))
