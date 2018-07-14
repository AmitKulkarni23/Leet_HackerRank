# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Credits -> https://www.youtube.com/watch?v=IFNibRVgFBo
    # Time Complexity -> O(n^3) -> We are finding subarrays
    # And for each subarray we are iterating from i to j

    # Space Complexity -> O(n^2)

    n = len(nums)

    if n == 0:
        return 0

    # Create a cache
    cache = [[0 for _ in range(n)] for _ in range(n)]

    for l in range(1, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j+1):
                left_val = 1
                right_val = 1

                if i != 0:
                    left_val = nums[i-1]

                if j != n - 1:
                    right_val = nums[j+1]


                before = 0
                after = 0

                if i != k:
                    before = cache[i][k-1]

                if j != k:
                    after = cache[k+1][j]

                cache[i][j] = max(left_val * nums[k] * right_val + before + after, cache[i][j])


    return cache[0][n-1]
