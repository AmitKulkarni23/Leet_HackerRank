"""
Given an integer array nums, find the contiguous
subarray (containing at least one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Solution: Use Kadane's Algorithm( GFG - https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_ending_here < 0)
            max_ending_here = 0
  (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far


"""


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_ending_here = 0
    max_so_far = float('-inf')

    # if nums is not empty
    if nums:
        for item in nums:
            max_ending_here += item

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                # Means we have encountered a -ve number
                max_ending_here = 0

        return max_so_far


# Example:
print(maxSubArray([-1]))