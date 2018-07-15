# You have a list of points in the plane. Return the area of the largest
# triangle that can be formed by any 3 of the points.
#
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation:
# The five points are show in the figure below. The red triangle is the largest.

import math
def largestTriangleArea(points):
    """
    :type points: List[List[int]]
    :rtype: float
    """
    # Credits -> https://leetcode.com/problems/largest-triangle-area/solution/
    # Use heron's formula
    # Area of triangle = sqrt(S * S -a * S - b * S - b)
    # where S = a + b + c / 2 and a, b, c are sides of triangle

    # Time COmplexity O(n^3)
    a, b, c, S = 0, 0, 0, 0
    max_area = 0

    pt_len = len(points)

    for i in range(pt_len):
        for j in range(i+1, pt_len):
            for k in range(j+1, pt_len):
                # get the lenght of teh 3 sides
                a = get_dist_bet_points(points[i], points[j])
                b = get_dist_bet_points(points[j], points[k])
                c = get_dist_bet_points(points[k], points[i])


                # Now we need to check if the triangle formed by these sides is valid
                if is_valid_triange(a, b, c):
                    S = (a + b + c) / 2
                    max_area = max(max_area, math.sqrt(S * (S - a) * (S - b) * (S - c)))
    return max_area

def get_dist_bet_points(pt1, pt2):
    """
    Returns the euclidean distance between 2 points
    """
    x = pt1[0] - pt2[0]
    y = pt1[1] - pt2[1]

    return math.sqrt(x * x + y * y)

def is_valid_triange(a, b, c):
    """
    Returns if a triangle can be formed by the 3 points
    """
    return a + b > c and b + c > a and a + c > b
# Examples
# points = [[0,0],[0,1],[1,0],[0,2],[2,0]]

points = [[1,0],[0,0],[0,1]]

# points = [[4,6],[6,5],[3,1]]
print(largestTriangleArea(points))
