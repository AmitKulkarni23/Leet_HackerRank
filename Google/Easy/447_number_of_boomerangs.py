# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]


def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """

    # Credits -> https://leetcode.com/problems/number-of-boomerangs/discuss/92868/Short-Python-O(n2)-hashmap-solution

    # IDEA: Create a dictionary to count all points with same distance
    # If for a point p, there are k points with distance d, number of boomerangs corresponding to that are k*(k-1).

    # Check out the circular image in the Credits link above

    numb_of_boomerangs = 0

    for p in points:
        dist_map = {}

        for q in points:
            x_dist = (p[0] - q[0]) ** 2
            y_dist = (p[1] - q[1]) ** 2

            dist_map[x_dist + y_dist] = 1 + dist_map.get(x_dist + y_dist, 0)

        for act_dist in dist_map.values():
            numb_of_boomerangs += act_dist * (act_dist - 1)


    return numb_of_boomerangs

# Examples

input = [[0,0],[1,0],[2,0]]
print(numberOfBoomerangs(input))
