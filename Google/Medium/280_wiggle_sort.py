# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
#
# Example:
#
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]

def wiggleSort(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # Credits -> https://leetcode.com/problems/wiggle-sort/solution/

    # Brute Force method:
    # Sorth the entire array first
    # then do a pairwise swapping of lements starting from teh second element

    #     [1, 2, 3, 4, 5, 6]
    #        ↑  ↑  ↑  ↑
    #        swap  swap
    #
    # => [1, 3, 2, 5, 4, 6]

    # Time COmplexity -> O(n log n)

    # One Pass Swap ( Time COmplexity -> O(n))
    # we should be able to reorder it in one-pass.
    # As we iterate through the array, we compare the current element to its
    # next element and if the order is incorrect, we swap them.

    for i in range(len(nums) - 1):
        if (((i % 2 == 0) and nums[i] > nums[i+1]) or ((i % 2 == 1) and nums[i] < nums[i+1])):
            # Then we need to swap the elements
            # call helper function swap_elements
            swap_elements(nums, i, i+1)


def swap_elements(nums, i, j):
    """
    Helper function to swap the elements at positions i and j in the array nums
    """
    nums[i], nums[j] = nums[j], nums[i]
