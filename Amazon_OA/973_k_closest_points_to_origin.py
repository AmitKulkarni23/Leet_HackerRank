# https://leetcode.com/problems/k-closest-points-to-origin/

# Brute Force -> Sort the elements by their distances to origin and return the first k elements
# return sorted(points, key=lambda item: item[0] ** 2 + item[1] ** 2)[:K]

# However this is O(NlogN) where N is the number of points.
# Use a max heap – Sort using a heap of size K
#
# Time - O(N log K)

import heapq
def kClosest(points, K):
    return heapq.nsmallest(K, points, key=lambda item: item[0] ** 2 + item[1] ** 2)
