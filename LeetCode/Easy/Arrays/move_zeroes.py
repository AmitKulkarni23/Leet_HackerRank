# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # Referred : https://leetcode.com/problems/move-zeroes/discuss/72012/Python-short-in-place-solution-with-comments.
    if nums:
        n = len(nums)
        zero = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
