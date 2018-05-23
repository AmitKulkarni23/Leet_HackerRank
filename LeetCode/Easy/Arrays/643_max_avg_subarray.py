# Given an array consisting of n integers, find the contiguous subarray of given length k
# that has the maximum average value. And you need to output the maximum average value.
#
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# Note:
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """

    # Credits : https://leetcode.com/problems/maximum-average-subarray-i/solution/
    # Time complexity : O(n)
    # Space complexity : O(n)
    
    sum_arr = [0] * len(nums)
    sum_arr[0] = nums[0]

    for i in range(1, len(nums)):
        sum_arr[i] = sum_arr[i - 1] + nums[i]

    res = sum_arr[k - 1] * 1.0 / k

    for i in range(k, len(nums)):
        res = max(res, (sum_arr[i] - sum_arr[i - k]) / k)

    return res


nums = [1,12,-5,-6,50,3]
k = 4

print(findMaxAverage(nums, k))
