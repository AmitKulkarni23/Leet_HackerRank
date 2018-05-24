# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
#              or index number 5 where the peak element is 6.
# Note:
#
# Your solution should be in logarithmic complexity.


def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Credits
    # VVIP : https://leetcode.com/problems/find-peak-element/solution/

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            # Then the peak lies in the left part of the array
            # Descending slope
            right = mid
        else:
            # Ascending slope
            left = mid + 1

    return left

# Examples:
arr = [1,2,3,1]
arr_2 = [1,2,1,3,5,6,4]
print(findPeakElement(arr_2))
