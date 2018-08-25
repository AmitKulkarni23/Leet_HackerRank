# Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.
#
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.

def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # Time Complexity -> O(log n)

    # Credits -> https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100732/Short-compare-numsi-with-numsi1

    # Find the first index which holds a different value
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] == nums[mid ^ 1]:
            low = mid + 1
        else:
            high = mid


    return nums[low]
