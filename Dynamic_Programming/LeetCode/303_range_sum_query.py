# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self.nums = nums
        # Cumulatively add all nums and store it data array
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]

        self.data = nums


    # Very Poor -> beats 23% of python submissions
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == j:
            return self.nums[i]

        return sum(self.nums[i:j+1])

    def sumRange_best_leet_code_solution(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.data[j]
        else:
            return self.data[j] - self.data[i-1]




# Your NumArray object will be instantiated and called as such:
nums = [1, 2, 3, 4, 7]
i = 2
j = 4
obj = NumArray(nums)
param_1 = obj.sumRange_best_leet_code_solution(i,j)
print(param_1)
