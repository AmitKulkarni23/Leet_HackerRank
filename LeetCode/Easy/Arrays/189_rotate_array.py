# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Note:
#
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    # Credits -> https://leetcode.com/problems/rotate-array/description/

    # Idea -> First reverse the given array
    # Then reverse the first k elements
    # Then reverse the next n - k elements

    k = k % len(nums)
    reverse_helper(nums, 0, len(nums) - 1)
    reverse_helper(nums, 0, k-1)
    reverse_helper(nums, k, len(nums)-1)

    return nums
def reverse_helper(nums, start, end):
    """
    Helper function to reverse the elements of array
    """
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1

# Examples
arr = [1, 2, 3, 4, 5, 6, 7]
n = 4
print(rotate(arr, n))
