# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # Credits : https://leetcode.com/problems/container-with-most-water/description/
    # Idea : Area is limited by the line with the shortest height
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


def best_leetcode_sol(height):
    """
    :type height: List[int]
    :rtype: int
    """
    area=0
    i=0
    j=len(height)-1
    while(i<j):
        if height[i]<height[j]:
            tmp=(j-i)*height[i]
            i+=1
            if tmp>area:
                area=tmp
        else:
            tmp=(j-i)*height[j]
            j-=1
            if tmp>area:
                area=tmp

    return area
