# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
#
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # Complexity -> O(log(min(len(x), len(y))))
    # We want to consider nums1's length to be smaller than length of nums2
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)

    x = len(nums1)
    y = len(nums2)

    low = 0
    high = x

    while low <= high:
        par_x = (low + high) // 2
        par_y = (x + y + 1) // 2 - par_x


        # Edge cases
        # if par_x <= 0, that means there is nothing on the left side
        if par_x == 0:
            max_left_x = float("-inf")
        else:
            max_left_x = nums1[par_x - 1]

        # if par_y == 0, that menas that there is on the left side
        if par_y == 0:
            max_left_y = float("-inf")
        else:
            max_left_y = nums2[par_y - 1]

        # if par_x == x, that measn there is nothing on the right side
        if par_x == x:
            min_right_x = float("inf")
        else:
            min_right_x = nums1[par_x]

        # if par_y == y, that measn there is nothing on the right side
        if par_y == y:
            min_right_y = float("inf")
        else:
            min_right_y = nums2[par_y]

        # Now comes the partitioning part
        # Case 1:
        # If we have partitioned the array at correct points

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (x + y) % 2 == 0:
                return float((max(max_left_x, max_left_y) + min(min_right_x, min_right_y))) / 2
            else:
                return max(max_left_x, max_left_y)

        elif max_left_x > min_right_y:
            high = par_x - 1
        else:
            low = par_x + 1


# nums1 = [1, 3, 8, 9, 15]
# nums2 = [7, 11, 19, 21, 18, 25]

nums1 = [1, 2]
nums2 = [3, 4]

print(findMedianSortedArrays(nums1, nums2))
