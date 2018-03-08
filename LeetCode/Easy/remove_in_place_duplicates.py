"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # This is solution is inspired by one of the
        # Python solutions in the discussion forum
        # https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/11751/Simple-Python-solution-O(n)
        
        if not nums:
            # If the array is empty
            return 0
        
        if len(nums) == 1:
            # If the array length is less than 1
            # return 1
            return 1
        
        prev_ind = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[prev_ind]:
                prev_ind += 1
                # Changing the array here
                nums[prev_ind] = nums[i]
        
        return prev_ind + 1